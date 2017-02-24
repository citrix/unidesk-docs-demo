from __future__ import print_function
from HTMLParser import HTMLParser
import os
import sys
import os.path
reload(sys)  # Reload is a hack
sys.setdefaultencoding('utf8')


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    start_tag = False
    mk_tag = ''
    relation_tp = []
    cotent_relation = []
    has_line = False
    in_header = False
    in_table = 0
    in_ul = 0
    in_ol = 0
    build_index = False
    num_th = 0
    line_content = ''
    output = ""
    link = ""
    hrefname = ""
    def unescape(self, s):
        s = s.replace("&lt;", "(LEFT)")
        s = s.replace("&gt;", "(RIGHT)")
        s = s.replace("&amp;", "(AND)")
        s = s.replace("&rsquo;", "(SINGLEQUOTE)")
        s = s.replace("&nbsp;", "(SPACE)")
        s = s.replace("&quot;", "(QUOTE)")
        return s

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == 'body':
            self.start_tag = True
        if self.start_tag:
            #print ("start"+tag)
            if self.in_table > 0 or self.in_ul > 0 or self.in_ol > 0:
                if tag == 'table':
                    self.in_table = self.in_table + 1
                elif tag == 'ul':
                    self.in_ul = self.in_ul + 1
                elif tag == 'ol':
                    self.in_ol = self.in_ol + 1
                if tag == 'a':
                    for attr in attrs:
                        if attr[0] == 'href': #it is a linked object
                            self.link = attr[1]
                    self.output = self.output + '<a href="' + self.link + '">'
                else:
                    self.output = self.output + '<' + tag + '>'
            elif tag == 'h1':
                self.mk_tag = '#'
                self.in_header = True
            elif tag == 'h2':
                self.mk_tag = '##'
                self.in_header = True
            elif tag == 'h3':
                self.mk_tag = '###'
                self.in_header = True
            elif tag == 'h4':
                self.mk_tag = '####'
                self.in_header = True
            elif tag == 'p':
                self.in_header = True
            elif tag == 'img':
                for attr in attrs:
                    if attr[0] == 'src': #it is a linked object
                        imgpath = attr[1]
                self.output = self.output + '![]('+imgpath+')'
                '''
                p_has_style = False
                #keep style in p and span
                for attr in attrs:
                    if attr[0] == 'style': #it is a referred object
                        p_has_style = True
                        style = attr[1].replace('\r', '').replace('\n', '')
                if p_has_style is True:
                    self.output = self.output + '<p style="'+ style + '">'
                else:
                    self.output = self.output + '<p>'
            elif tag == 'span':
                #keep style in p and span
                span_has_style = False
                for attr in attrs:
                    if attr[0] == 'style': #it is a referred object
                        span_has_style = True
                        style = attr[1].replace('\r', '').replace('\n', '')
                if span_has_style is True:
                    self.output = self.output + '<span style="'+ style + '">'
                else:
                    self.output = self.output + '<span>'
                '''
            elif tag == 'th':
                self.mk_tag = '|'
                self.num_th = self.num_th + 1
            elif tag == 'td':
                self.mk_tag = '|'
            elif tag == 'tr':
                self.has_line = True
            elif tag == 'code':
                self.mk_tag = ""
                self.output = self.output + "```" + "\r"
            elif tag == 'a':
                if self.in_header is True: #a in included in a line
                    for attr in attrs:
                        if attr[0] == 'name' and self.build_index is True: #it is a referred object
                            self.relation_tp.append(attr[1])
                            self.hrefname = self.hrefname + '<a name="'+ attr[1] + '"></a>'
                        elif attr[0] == 'href': #it is a linked object
                            self.link = attr[1]
                            self.mk_tag = 'a'
                else: #a is a line
                    output_list = self.output.split("\r")
                    output_list.pop(-1) #Do not breakline for a start
                    join_tag = "\r"
                    self.output = join_tag.join(output_list)
                    self.mk_tag = 'a'
                    for attr in attrs:
                        if attr[0] == 'href': #href means it is a linked object
                            self.link = attr[1]
            elif tag == 'em' or tag == 'strong':
                self.mk_tag = "em"
            elif tag == 'table':
                self.in_table = self.in_table + 1
                self.output = self.output + '<table>'
            elif tag == 'ul':
                self.in_ul = self.in_ul + 1
                self.output = self.output + '<ul>'
            elif tag == 'ol':
                self.in_ol = self.in_ol + 1
                self.output = self.output + '<ol>'
            else:
                self.mk_tag = ""

    def handle_data(self, data):
        data = data.replace('\r', "").replace('\n', "")
        data = data.replace('(LEFT)', "<").replace('(RIGHT)', ">").replace('(SINGLEQUOTE)', "'").replace('(AND)', ";").replace('(SPACE)', " ").replace('(QUOTE)', "\"")
        #data = data.replace('(LEFT)',"&lt;").replace('(RIGHT)',"&gt;")
        if self.start_tag and data != "":
            #print ("data"+data)
            if self.in_table > 0 or self.in_ul > 0 or self.in_ol > 0:
                self.output = self.output + data
            elif self.mk_tag == '|':
                self.line_content = self.line_content + self.mk_tag + data
            elif self.mk_tag == 'a':
                #Need to check if the link is abcd.html, if so, remove html
                if self.link[-5:] == '.html' and len((self.link).split(".")) == 2:
                    self.link = self.link[:-5]
                elif self.link[-4:] == '.htm' and len((self.link).split(".")) == 2:
                    self.link = self.link[:-4]
                self.output = self.output + "[" + data + "]("+ self.link + ")"
                if self.in_header is False:
                    self.output = self.output + "\r\n"
            elif self.mk_tag == 'em':
                self.output = self.output + "***" + data + "*** "
            else:
                if self.in_header is True and self.build_index is True and len(self.relation_tp) > 0:
                    self.cotent_relation.append({"data":data, "name":self.relation_tp})
                if data.strip() != '':
                    try:
                        data = data.encode('utf-8', 'strict')
                    except:
                        data = data.replace('\x92',"'").replace('\x93','').replace('\x91','').replace('\x94','').encode('utf-8', 'strict')
                    self.output = self.output + self.mk_tag + data + self.hrefname

    def handle_endtag(self, tag):
        tag = tag.lower()
        join_tag = "\r"
        output_list = self.output.split("\r")
        if self.start_tag is True:
            #print ("end"+tag)
            if self.in_table > 0 or self.in_ul > 0 or self.in_ol > 0:
                self.output = self.output + "</" + tag + ">"
                if tag == 'table':
                    self.in_table = self.in_table - 1
                    if self.in_table == 0 and self.in_ul == 0 and self.in_ol == 0:
                        self.output = self.output + "\r\n"
                elif tag == 'ul':
                    self.in_ul = self.in_ul - 1
                    if self.in_table == 0 and self.in_ul == 0 and self.in_ol == 0:
                        self.output = self.output + "\r\n"
                elif tag == 'ol':
                    self.in_ol = self.in_ol - 1
                    if self.in_table == 0 and self.in_ul == 0 and self.in_ol == 0:
                        self.output = self.output + "\r\n"
            elif tag == 'h1' or tag == 'h2' or tag == 'h3' or tag == 'h4' or tag == 'p':
                self.in_header = False
                self.relation_tp = []
                self.hrefname = ''
                self.mk_tag = ''
                if self.in_table == 0 and self.in_ul == 0 and self.in_ol == 0:
                    self.output = self.output + "\r\n"
            elif tag == 'div':
                if self.in_table == 0 and self.in_ul == 0 and self.in_ol == 0:
                    self.output = self.output + "\r\n"
            elif tag == 'code':
                lastline = output_list[-2].strip()
                if lastline == "```":
                    output_list[-2] = "\n"
                    print (lastline)
                    self.output = join_tag.join(output_list)
                else:
                    self.output = self.output + "```"+ "\r\n"  #print ("```")
            elif tag == 'a' and self.in_header is False:
                self.mk_tag = ''
            elif tag == 'em' or tag == 'strong':
                self.mk_tag = ''
            elif tag == 'body':
                pass
                #return self.cotent_relation
            '''
            elif tag == 'p':
                self.in_header = False
                self.relation_tp = []
                self.hrefname = ''
                self.mk_tag = ''
                if self.in_table == 0 and self.in_ul == 0 and self.in_ol == 0:
                    self.output = self.output + "</p>\r\n"
            elif tag == 'span':
                self.output = self.output + "</span>"
            '''
            #elif tag == 'tr':
            #    self.output = self.output+self.line_content+'|'+ "\r"#print (self.line_content+'|')
            #    if self.num_th != 0:
            #        line = ''
            #        i = 0
            #        while i < self.num_th:
            #            line = line + '|--'
            #            i = i + 1
                    #print (line + '|')
            #        self.output = self.output + line + '|'+ "\r"
            #        self.num_th = 0
            #    self.has_line = False
            #    self.line_content = ''

def iconv(exepath, inputf, temp):
    win_cmd = exepath + ' -f UCS-2LE -t utf-8 ' + inputf +' > '+ temp
    os.system(win_cmd)
    #process = subprocess.Popen(win_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #for line in process.stdout:
    #    print(line)
    os.remove(inputf)
    os.rename(temp, inputf)

def print_no_line(st):
    print (st, end='')

def process_single(path,filename,convert):
    iconvexe = "C:\\Users\\haow\\Desktop\\html2mk\\iconv.exe" #File encoder path
    parser = MyHTMLParser()
    parser.build_index = True
    inputf = path + '\\' + filename+'.htm'
    input_file = open(inputf, 'r')
    if convert is True:
        tempf = path + '\\' + 'temp.htm'
        iconv(iconvexe, inputf, tempf)
    output_file = open(path + '\\' + filename+'.md', 'w')
    input_content = input_file.read()
    input_content = parser.unescape(input_content)
    parser.feed(input_content)
    #cotent_relation = parser.cotent_relation #Get relationship
    output_file.write(parser.output)
    input_file.close()
    output_file.close()

def process_mutiple(rootpath, org_rootpath):
    for root, dirs, files in os.walk(rootpath):
        #print ("###", root,dirs,files,len(root.split(org_rootpath)[1].split('\\')))
        level = len(root.split(org_rootpath)[1].split('\\'))
        while level > 2:
            print_no_line("    ")
            level = level - 1
        rear = root.split(org_rootpath)[1]
        if '\\' in rear:
            print ("- "+rear.split("\\")[-1] + ":")

        '''
        for directory in dirs:
            print ("DIRDIR")
            level = iteration
            while level > 0:
                print_no_line("    ")
                level = level - 1
            print ("- "+directory+":")
            subpath = root + "\\" + directory
            nextiteration = iteration + 1
            print ("?????"+ subpath +"?"+ org_rootpath + "?" + str(nextiteration))
            process_mutiple(subpath, org_rootpath, nextiteration)
        '''
        for filename in files:
            path = os.path.join(root, filename)
            if os.path.exists(path) and filename[-4:] == '.htm':
                level = len(root.split(org_rootpath)[1].split('\\'))
                while level > 1:
                    print_no_line("    ")
                    level = level - 1
                name = filename[:-4]
                #path = os.path.join(root, filename)
                print("- "+ name +": "+ path.split(org_rootpath)[1][1:][:-4]+'.md')
                process_single(root, name, False)

def main():
    rootpath = "C:\\Users\\haow\\Desktop\\SDK\\docs"
    #name = 'pvssdk'
    #process_single(rootpath, name, False)
    process_mutiple(rootpath, rootpath)

main()
