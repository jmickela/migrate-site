import django
django.setup()

from django.db import connections
from django.db.utils import ConnectionDoesNotExist

from content.models import NewsItem, PressRelease, OtherContent

# Row IDs for the data in the current database.
OLD_ID = 0
TITLE = 1
SUB_TITLE = 2
BODY = 3
AUTHOR = 4
UPDATED = 5
TYPE = 6
PUBLISH = 8
LINKTEXT = 9
DOC = 16
LINK = 20
SUMMARY = 22
DATE = 23
PICTURE = 28
SOURCE = 34
CONTACT = 35
CREATED = 40
SOURCEURL = 42
MEDIA_HTML = 57
MEDIA_THUMB = 59


def setup_cursor():
    # Get a cursor for the legacy database defined in the django project settings.
    try:
        cursor = connections['legacy'].cursor()
        return cursor
    except ConnectionDoesNotExist:
        print "Legacy database is not configured"
        return None


def import_news_items():
    cursor = setup_cursor()
    if cursor is None:
        return
    ## it's important selecting the id field, so that we can keep the publisher - book relationship
    sql = """select * from articles left join articletype on articles.type = articletype.id WHERE articles.publish = 1 AND (articletype.parent = 42 or articletype.id = 42);"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        old_id = row[OLD_ID]
        title = row[TITLE]
        subtitle = row[SUB_TITLE]
        body = row[BODY]
        type = row[TYPE]
        summary = row[SUMMARY]
        date = row[DATE]
        datecreated = row[CREATED]
        author = row[AUTHOR]
        updated = row[UPDATED]
        sourceurl = row[SOURCEURL]
        publish = row[PUBLISH]
        linktext = row[LINKTEXT]
        link = row[LINK]
        docname = row[DOC]
        picture = row[PICTURE]
        source = row[SOURCE]
        contact = row[CONTACT]
        media = row[MEDIA_HTML]
        media_thumb_url = row[MEDIA_THUMB]
        news_item = NewsItem(
            old_id=old_id,
            title=title,
            subtitle=subtitle,
            body=body,
            old_type=type,
            summary=summary,
            date=date,
            datecreated=datecreated,
            author=author,
            updated=updated,
            sourceurl=sourceurl,
            publish=publish,
            linktext=linktext,
            link=link,
            docname=docname,
            picture=picture,
            source=source,
            contact=contact,
            media=media,
            media_thumb_url=media_thumb_url)

        try:
            news_item.save()
        except Exception as e:
            print str(e)

def import_press_release():
    cursor = setup_cursor()
    if cursor is None:
        return
    sql = """select * from articles left join articletype on articles.type = articletype.id WHERE articles.publish=1 AND (articletype.parent = 16 or articletype.id = 16);"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        old_id = row[OLD_ID]
        title = row[TITLE]
        subtitle = row[SUB_TITLE]
        body = row[BODY]
        type = row[TYPE]
        summary = row[SUMMARY]
        date = row[DATE]
        datecreated = row[CREATED]
        author = row[AUTHOR]
        updated = row[UPDATED]
        sourceurl = row[SOURCEURL]
        publish = row[PUBLISH]
        linktext = row[LINKTEXT]
        link = row[LINK]
        docname = row[DOC]
        picture = row[PICTURE]
        source = row[SOURCE]
        contact = row[CONTACT]
        media = row[MEDIA_HTML]
        media_thumb_url = row[MEDIA_THUMB]
        news_item = PressRelease(
            old_id=old_id,
            title=title,
            subtitle=subtitle,
            body=body,
            old_type=type,
            summary=summary,
            date=date,
            datecreated=datecreated,
            author=author,
            updated=updated,
            sourceurl=sourceurl,
            publish=publish,
            linktext=linktext,
            link=link,
            docname=docname,
            picture=picture,
            source=source,
            contact=contact,
            media=media,
            media_thumb_url=media_thumb_url)

        try:
            news_item.save()
        except Exception as e:
            print str(e)

def import_other_content():
    cursor = setup_cursor()
    if cursor is None:
        return
    ## it's important selecting the id field, so that we can keep the publisher - book relationship
    sql = """select * from articles left join articletype on articles.type = articletype.id WHERE articles.publish=1 AND NOT (articletype.parent = 16 OR articletype.id = 16 OR articletype.parent = 42 OR articletype.id = 42);"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        old_id = row[OLD_ID]
        title = row[TITLE]
        subtitle = row[SUB_TITLE]
        body = row[BODY]
        type = row[TYPE]
        summary = row[SUMMARY]
        date = row[DATE]
        datecreated = row[CREATED]
        author = row[AUTHOR]
        updated = row[UPDATED]
        sourceurl = row[SOURCEURL]
        publish = row[PUBLISH]
        linktext = row[LINKTEXT]
        link = row[LINK]
        docname = row[DOC]
        picture = row[PICTURE]
        source = row[SOURCE]
        contact = row[CONTACT]
        media = row[MEDIA_HTML]
        media_thumb_url = row[MEDIA_THUMB]
        news_item = OtherContent(
            old_id=old_id,
            title=title,
            subtitle=subtitle,
            body=body,
            old_type=type,
            summary=summary,
            date=date,
            datecreated=datecreated,
            author=author,
            updated=updated,
            sourceurl=sourceurl,
            publish=publish,
            linktext=linktext,
            link=link,
            docname=docname,
            picture=picture,
            source=source,
            contact=contact,
            media=media,
            media_thumb_url=media_thumb_url)

        try:
            news_item.save()
        except Exception as e:
            print str(e)

def main():
    import_news_items()
    import_press_release()
    import_other_content()

if __name__=="__main__":
    main()