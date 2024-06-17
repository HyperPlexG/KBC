def get_question(n, t):
  return a[n][t]

a = [[0 for i in range(10)] for i in range(15)]

# a[i][j] = ["question", "option A", "option B", "option C", "option D", "correct answer"]

a[0][0] = ["What does HTML stand for?", "Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "Hyper Text Markup Leveler", "Hyper Text Markup Language"]
a[0][1] = ["What is the main function of a web browser?", "To edit images", "To browse the internet", "To play music", "To compile code", "To browse the internet"]
a[0][2] = ["Which company developed the iPhone?", "Microsoft", "Google", "Apple", "Amazon", "Apple"]
a[0][3] = ["What is the basic unit of information in computing?", "Byte", "Bit", "Pixel", "Node", "Bit"]
a[0][4] = ["Which social media platform is known for its 'Like' button?", "Twitter", "Instagram", "LinkedIn", "Facebook", "Facebook"]

a[1][0] = ["Which programming language is known for its snake logo?", "Ruby", "Python", "Java", "C++", "Python"]
a[1][1] = ["What does CPU stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Print Unit", "Control Processing Unit", "Central Processing Unit"]
a[1][2] = ["What company is known for the Windows operating system?", "Apple", "Microsoft", "IBM", "Google", "Microsoft"]
a[1][3] = ["What is the name of Microsofts cloud computing service?", "Azure", "AWS", "Google Cloud", "IBM Cloud", "Azure"]
a[1][4] = ["What technology is used to make telephone calls over the Internet?", "VoIP", "LTE", "ISDN", "DSL", "VoIP"]

a[2][0] = ["Which company created the Android operating system?", "Apple", "Microsoft", "Google", "IBM", "Google"]
a[2][1] = ["What does USB stand for?", "Universal System Bus", "Universal Serial Bus", "Unique Serial Bus", "Universal Service Bus", "Universal Serial Bus"]
a[2][2] = ["Which device is primarily used for pointing and clicking?", "Keyboard", "Monitor", "Mouse", "Printer", "Mouse"]
a[2][3] = ["What is the name of the first electronic general-purpose computer?", "ENIAC", "UNIVAC", "IBM PC", "Altair 8800", "ENIAC"]
a[2][4] = ["Which company is known for its search engine?", "Yahoo", "Google", "Bing", "DuckDuckGo", "Google"]

a[3][0] = ["What is the most popular programming language for web development?", "C++", "Python", "JavaScript", "PHP", "JavaScript"]
a[3][1] = ["What is the term for a network security system that monitors and controls incoming and outgoing network traffic?", "Router", "Firewall", "Modem", "Switch", "Firewall"]
a[3][2] = ["Which company developed the video game 'Minecraft'?", "Electronic Arts", "Mojang", "Ubisoft", "Blizzard Entertainment", "Mojang"]
a[3][3] = ["Which protocol is used for secure communication over a computer network?", "HTTP", "FTP", "HTTPS", "SMTP", "HTTPS"]
a[3][4] = ["What does SQL stand for?", "Structured Query Language", "Sequential Query Language", "Simple Query Language", "Structured Question Language", "Structured Query Language"]

a[4][0] = ["Who is known as the father of the computer?", "Bill Gates", "Charles Babbage", "Steve Jobs", "Alan Turing", "Charles Babbage"]
a[4][1] = ["What is the primary function of RAM in a computer?", "To store permanent data", "To store temporary data", "To process instructions", "To manage network traffic", "To store temporary data"]
a[4][2] = ["Which language is primarily used for iOS app development?", "Kotlin", "Swift", "Java", "Python", "Swift"]
a[4][3] = ["What does LAN stand for?", "Long Area Network", "Local Area Network", "Light Area Network", "Line Area Network", "Local Area Network"]
a[4][4] = ["Which of these is an example of an open-source operating system?", "Windows", "macOS", "Linux", "Android", "Linux"]

a[5][0] = ["Which company is known for creating the first graphical web browser?", "Netscape", "Microsoft", "Google", "Apple", "Netscape"]
a[5][1] = ["What year was the World Wide Web introduced to the public?", "1985", "1990", "1991", "1993", "1991"]
a[5][2] = ["What is the most popular open-source version control system?", "SVN", "Mercurial", "Git", "CVS", "Git"]
a[5][3] = ["Which programming language is primarily used for artificial intelligence?", "Java", "Python", "C#", "Ruby", "Python"]
a[5][4] = ["What does DNS stand for?", "Dynamic Name System", "Dynamic Network Service", "Domain Name System", "Domain Network Service", "Domain Name System"]

a[6][0] = ["Which of these is a version of Linux?", "Windows", "Ubuntu", "macOS", "Android", "Ubuntu"]
a[6][1] = ["What does HTTP stand for?", "HyperText Transfer Protocol", "HyperText Transmission Protocol", "HyperText Transfer Program", "HyperText Transmission Program", "HyperText Transfer Protocol"]
a[6][2] = ["Which company developed the Java programming language?", "Microsoft", "Apple", "Sun Microsystems", "IBM", "Sun Microsystems"]
a[6][3] = ["What is the primary protocol used to send email?", "HTTP", "FTP", "SMTP", "IMAP", "SMTP"]
a[6][4] = ["Which cloud computing platform is provided by Amazon?", "Azure", "Google Cloud", "AWS", "IBM Cloud", "AWS"]

a[7][0] = ["What does GUI stand for?", "Graphical User Interface", "Graphical Usage Interface", "General User Interface", "General Usage Interface", "Graphical User Interface"]
a[7][1] = ["Which programming language is known for its use in data science?", "C++", "R", "Swift", "PHP", "R"]
a[7][2] = ["What is the name of the company that owns the Android operating system?", "Google", "Apple", "Microsoft", "Samsung", "Google"]
a[7][3] = ["What does GPU stand for?", "Graphics Processing Unit", "General Processing Unit", "Graphics Power Unit", "General Power Unit", "Graphics Processing Unit"]
a[7][4] = ["What is the primary markup language used for creating web pages?", "HTML", "CSS", "JavaScript", "PHP", "HTML"]

a[8][0] = ["Which company is known for the creation of the Linux kernel?", "Microsoft", "Apple", "IBM", "Linus Torvalds", "Linus Torvalds"]
a[8][1] = ["What is the name of the cloud computing platform developed by Google?", "Azure", "Google Cloud Platform", "AWS", "Oracle Cloud", "Google Cloud Platform"]
a[8][2] = ["Which software is used to view websites?", "Word Processor", "Spreadsheet", "Browser", "Database", "Browser"]
a[8][3] = ["Which of the following is a type of non-volatile memory?", "RAM", "ROM", "Cache", "Register", "ROM"]
a[8][4] = ["What does IoT stand for?", "Internet of Things", "Internet of Technology", "Internet of Tools", "Internet of Toys", "Internet of Things"]

a[9][0] = ["Which language is primarily used for Android app development?", "Swift", "Kotlin", "Java", "C#", "Java"]
a[9][1] = ["What is the name of Apple's personal assistant?", "Cortana", "Alexa", "Siri", "Google Assistant", "Siri"]
a[9][2] = ["What type of software is used for creating spreadsheets?", "Database", "Word Processor", "Spreadsheet", "Presentation", "Spreadsheet"]
a[9][3] = ["Which of these is a popular cloud storage service?", "Dropbox", "WordPress", "Apache", "MySQL", "Dropbox"]
a[9][4] = ["Which company developed the iOS operating system?", "Google", "Microsoft", "Apple", "IBM", "Apple"]

a[10][0] = ["What does VR stand for?", "Virtual Reality", "Virtual Resource", "Virtual Response", "Virtual Router", "Virtual Reality"]
a[10][1] = ["What is the main purpose of a firewall?", "To connect networks", "To protect against malware", "To provide WiFi", "To display web pages", "To protect against malware"]
a[10][2] = ["What does SSL stand for?", "Secure Socket Layer", "Secure Software Layer", "Secure System Link", "Secure System Layer", "Secure Socket Layer"]
a[10][3] = ["Which of the following is a relational database management system?", "MySQL", "NoSQL", "HDFS", "XML", "MySQL"]
a[10][4] = ["Which of these programming languages is primarily used for scientific computing?", "JavaScript", "Fortran", "Swift", "PHP", "Fortran"]

a[11][0] = ["What does AI stand for?", "Automated Interface", "Advanced Integration", "Artificial Intelligence", "Automated Intelligence", "Artificial Intelligence"]
a[11][1] = ["What is the main programming language used in Apple's development environment?", "Java", "Objective-C", "Swift", "C#", "Swift"]
a[11][2] = ["Which of these is a front-end web development framework?", "Django", "Laravel", "React", "Flask", "React"]
a[11][3] = ["Which company developed the video game console 'PlayStation'?", "Nintendo", "Sony", "Microsoft", "Sega", "Sony"]
a[11][4] = ["What is the purpose of an API?", "To secure data", "To provide a user interface", "To allow different systems to communicate", "To manage databases", "To allow different systems to communicate"]

a[12][0] = ["What does HTTP stand for?", "HyperText Transfer Protocol", "HyperText Transmission Protocol", "HyperText Transfer Program", "HyperText Transmission Program", "HyperText Transfer Protocol"]
a[12][1] = ["What is the primary language used for Android app development?", "Swift", "Kotlin", "Java", "C#", "Java"]
a[12][2] = ["What technology is primarily used to create web applications?", "HTML", "JavaScript", "CSS", "Python", "JavaScript"]
a[12][3] = ["What does DNS stand for?", "Dynamic Name System", "Dynamic Network Service", "Domain Name System", "Domain Network Service", "Domain Name System"]
a[12][4] = ["Which language is primarily used for statistical analysis?", "Python", "Java", "R", "Ruby", "R"]

a[13][0] = ["What is the main purpose of a database index?", "To store data", "To ensure data integrity", "To speed up query processing", "To maintain database connections", "To speed up query processing"]
a[13][1] = ["What does JSON stand for?", "JavaScript Object Notation", "Java Standard Output Notation", "JavaScript Oriented Notation", "Java Serialized Object Notation", "JavaScript Object Notation"]
a[13][2] = ["What is the key component of a computer's operating system that manages hardware and software resources?", "Kernel", "BIOS", "Cache", "Firmware", "Kernel"]
a[13][3] = ["What does SaaS stand for?", "Software as a Service", "Storage as a Service", "Security as a Service", "Support as a Service", "Software as a Service"]
a[13][4] = ["Which database model uses tables to organize data?", "Hierarchical", "Network", "Relational", "Object-oriented", "Relational"]

