import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("日志源码")
r2=s2.getRootTopic()
r2.setTitle("日志源码")


content={

'DefaultLogEventFactory':[
    '实现LogEventFactory接囗，重写其方法',
    {'createEvent(final String loggerName, ...)':[
        'new Log4jLogEvent(loggerName, marker, fqcn, level, data, properties, t);',
    ]}
],
'AbstractFilterable':[
    {'isFiltered':[
        'return filter != null && filter.filter(event) == Filter.Result.DENY;'
    ]}
],
'AppenderControl':[
    'ThreadLocal<AppenderControl> recursive = new ThreadLocal<>();',
    {'callAppender(final LogEvent event)':[
        'if (shouldSkip(event)) {',
        '   return;',
        'callAppenderPreventRecursion(event);'
    ]},
    {'shouldSkip(final LogEvent event)':[
        'return isFilteredByAppenderControl(event) || isFilteredByLevel(event) || isRecursiveCall();'
    ]},
    {'callAppenderPreventRecursion(final LogEvent event)':[
        ' try {',
        '   recursive.set(this);',
        '   callAppender0(event);',
        '} finally {',
        '   recursive.set(null);',
        '}'      
    ]},
    {'callAppender0(final LogEvent event)':[
        'ensureAppenderStarted();',
        'if (!isFilteredByAppender(event)) {',
        '   tryCallAppender(event);',
        '}'
    ]},
    {'ensureAppenderStarted()':[
        'if (!appender.isStarted()) {',
        '   handleError("Attempted to append to non-started appender ");',
        '}'
    ]},
    {'isFilteredByAppender(final LogEvent event)':[
        'return appender instanceof Filterable && ((Filterable) appender).isFiltered(event);'
    ]},
    {'tryCallAppender(final LogEvent event)':[
        'appender.append(event);'
    ]}
],
'AbstractOutputStreamAppender':[
    {'append(final LogEvent event)':[
        'tryAppend(event);'
    ]},
    {'tryAppend(final LogEvent event)':[
        'if (Constants.ENABLE_DIRECT_ENCODERS) {',
        '   directEncodeEvent(event);',
        '} else {',
        '   writeByteArrayToManager(event);',
        '}'           
    ]},
    {'directEncodeEvent(final LogEvent event)':[
        'getLayout().encode(event, manager);',
        'if (this.immediateFlush || event.isEndOfBatch()) {',
        '   manager.flush();',
        '}'
    ]}
],
'PatternLayout':[
    {'encode':[
        'encoder.encode(text, destination);'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 