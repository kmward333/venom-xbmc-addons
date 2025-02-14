# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# source 33 date created 24/11/2020
return False  # CF depuis le 26/11/2020
import re

from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress  # , VSlog

SITE_IDENTIFIER = 'filmoflix'
SITE_NAME = 'Filmoflix'
SITE_DESC = ' films et series'

URL_MAIN = 'https://www.filmoflix.org/'

MOVIE_NEWS = (URL_MAIN + 'filmsenstreaming/', 'showMovies')
MOVIE_GENRES = (True, 'showMovieGenres')

SERIE_NEWS = (URL_MAIN + 'seriesenstreaming/', 'showMovies')
SERIE_GENRES = (True, 'showSerieGenres')
SERIE_VF = (URL_MAIN + 'seriesenstreaming/series-vf/', 'showMovies')
SERIE_VOSTFR = (URL_MAIN + 'seriesenstreaming/series-vostfr/', 'showMovies')

key_search_movies = '#searchsomemovies'
key_search_series = '#searchsomeseries'
URL_SEARCH = (URL_MAIN + 'index.php?do=search', 'showMovies')
URL_SEARCH_MOVIES = (key_search_movies, 'showMovies')
URL_SEARCH_SERIES = (key_search_series, 'showMovies')

# recherche utilisé quand on n'utilise pas le globale
MY_SEARCH_MOVIES = (True, 'myShowSearchMovie')
MY_SEARCH_SERIES = (True, 'myShowSearchSerie')

# Menu GLOBALE HOME
MOVIE_MOVIE = (True, 'showMoviesSource')
SERIE_SERIES = (True, 'showTvshowSource')


def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_SEARCH[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche Films & Series', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_MOVIES[1], 'Recherche Films', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_SERIES[1], 'Recherche Series ', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Series (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Serie (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Series (VF)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Serie (VOST)', 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMoviesSource():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_MOVIES[1], 'Recherche Films', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showTvshowSource():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_SERIES[1], 'Recherche Series ', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Series (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Serie(Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Series (VF)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Serie(VOST)', 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def myShowSearchSerie():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = key_search_movies + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def myShowSearchMovie():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = key_search_series + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showMovieGenres():
    showGenres(URL_MAIN + 'filmsenstreaming/', '')


def showSerieGenres():
    showGenres(URL_MAIN + 'seriesenstreaming/', '-s')


def showGenres(urltype, s):
    oGui = cGui()

    liste = []
    listegenre = ['action', 'animation', 'aventure', 'biopic', 'comedie', 'drame', 'documentaire', 'epouvante-horreur',
                  'espionnage', 'famille', 'fantastique', 'guerre', 'historique', 'policier', 'romance',
                  'science-fiction', 'thriller', 'western']

    # https://www.filmoflix.net/filmsenstreaming/action/
    # https://www.filmoflix.net/seriesenstreaming/action-s/

    for igenre in listegenre:
        liste.append([igenre.capitalize(), urltype + igenre + s + '/'])

    oOutputParameterHandler = cOutputParameterHandler()
    for sTitle, sUrl in liste:
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    bSearchMovie = False
    bSearchSerie = False

    if sSearch:
        # sUrl = URL_SEARCH[0] # sert a rien
        sSearch = sSearch.replace(' ', '+').replace('%20', '+')

        if key_search_movies in sSearch:
            sSearch = sSearch.replace(key_search_movies, '')
            bSearchMovie = True
        if key_search_series in sSearch:
            sSearch = sSearch.replace(key_search_series, '')
            bSearchSerie = True

        pdata = 'do=search&subaction=search&search_start=0&full_search=0&result_from=1&story=' + sSearch
        oRequest = cRequestHandler(URL_SEARCH[0])
        oRequest.setRequestType(1)
        oRequest.addHeaderEntry('Referer', URL_MAIN)
        oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        oRequest.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
        oRequest.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
        oRequest.addParametersLine(pdata)
        sHtmlContent = oRequest.request()

    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()

    # ref thum title years
    sPattern = 'class="th-item".+?.+?ref="([^"]*).+?src="([^"]*).+?alt="([^"]*).+?Date.+?<.span>([^<]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):

        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sUrl2 = aEntry[0]
            sThumb = aEntry[1]
            sTitle = aEntry[2]
            sYear = aEntry[3].strip()

            if bSearchMovie:
                if '/serie' in sUrl2:
                    continue
            if bSearchSerie:
                if '/serie' not in sUrl2:
                    continue

            sDisplayTitle = sTitle
            if sSearch and not bSearchMovie and not bSearchSerie:
                if '/serie' in sUrl2:
                    sDisplayTitle = sDisplayTitle + ' [serie]'
                else:
                    sDisplayTitle = sDisplayTitle + ' [film]'

            # VSlog(sUrl2 );VSlog(sTitle);VSlog(sThumb );VSlog(sYear  )

            sDisplayTitle = sDisplayTitle + ' (' + sYear + ')'
            if 'http' not in sThumb:
                sThumb = URL_MAIN[:-1] + sThumb

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sYear', sYear)

            if '/series' not in sUrl2:
                oGui.addMovie(SITE_IDENTIFIER, 'showMovieLinks', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)
            else:
                oGui.addTV(SITE_IDENTIFIER, 'showSaisons', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)

        progress_.VSclose(progress_)

    if not sSearch:
        bNextPage, sNextPage, sNumPage = __checkForNextPage(sHtmlContent)
        if (bNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', 'Page ' + sNumPage, oOutputParameterHandler)

        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()
    sNextPage = ''
    snumberNext = ''
    sNumberMax = ''
    sNumPage = ''

    if '<div class="pnext' not in sHtmlContent:
        return False, 'none', 'none'

    sPattern = '(\d+)<.a><.div>.+?<div class="pnext">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sNumberMax= aResult[1][0]

    sPattern = '<div class="pnext">.+?href="([^"]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sNextPage = aResult[1][0]  # minimum requis
        try:
            snumberNext = re.search('page.([0-9]+)', sNextPage).group(1)
        except:
            pass

    if snumberNext:
        sNumPage = snumberNext
        if sNumberMax:
            sNumPage = sNumPage + '/' + sNumberMax
    if sNextPage:
        return True, sNextPage, sNumPage

    return False, 'none', 'none'


def showSaisons():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sYear = oInputParameterHandler.getValue('sYear')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = 'property="og:description".+?content="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sDesc = 'FilmoFlix'
    if (aResult[0] == True):
        sDesc = ('[I][COLOR grey]%s[/COLOR][/I] %s') % ('Synopsis :', aResult[1][0])

    sPattern = 'th-item">.+?href="([^"]*).+?src="([^"]*).+?title.+?>([^<]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in reversed(aResult[1]):

            sUrl2 = aEntry[0]
            sThumb = aEntry[1]
            sSaison = aEntry[2]  # SAISON 2

            if 'http' not in sThumb:
                sThumb = URL_MAIN[:-1] + sThumb

            sTitle = ("%s %s (%s)") % (sMovieTitle, sSaison, sYear)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sSaison', sSaison)

            oGui.addEpisode(SITE_IDENTIFIER, 'ShowEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def ShowEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sYear = oInputParameterHandler.getValue('sYear')
    sSaison = oInputParameterHandler.getValue('sSaison')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '(?:class="saisontab">.+?|<.a>)<a\shref="([^"]*).+?fsa-ep">([^<]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sUrl2 = aEntry[0]
            sEpisode = aEntry[1].replace('é', 'e').strip()  # épisode 2
            if 'http' not in sUrl2:
                sUrl2 = URL_MAIN[:-1] + sUrl2

            sTitle = sMovieTitle + ' ' + sSaison + ' ' + sEpisode + ' (' + sYear + ')'

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addEpisode(SITE_IDENTIFIER, 'showSerieLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSerieLinks():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sYear = oInputParameterHandler.getValue('sYear')

    oParser = cParser()
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    cook = oRequestHandler.GetCookies()

    sPattern = "class=\"lien.+?playEpisode.+?\'([^\']*).+?'([^\']*)"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            id = aEntry[0]
            xfield = aEntry[1]
            hostename = xfield.replace('_', ' ').replace('vf', 'VF')

            postdata = 'id=' + id + '&xfield=' + xfield + '&action=playEpisode'
            sUrl2 = URL_MAIN + 'engine/inc/serial/app/ajax/Season.php'

            sDisplayTitle = ('%s [COLOR coral]%s[/COLOR]') % (sTitle + ' (' + sYear + ')', hostename)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('referer', sUrl)
            oOutputParameterHandler.addParameter('cook', cook)
            oOutputParameterHandler.addParameter('postdata', postdata)

            oGui.addLink(SITE_IDENTIFIER, 'showSerieHosters', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSerieHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    referer = oInputParameterHandler.getValue('referer')
    # cook = oInputParameterHandler.getValue('cook')
    postdata = oInputParameterHandler.getValue('postdata')

    oRequest = cRequestHandler(sUrl)
    oRequest.setRequestType(1)
    oRequest.addHeaderEntry('Referer', referer)
    oRequest.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
    # oRequest.addHeaderEntry('Cookie', cook) # pas besoin ici mais besoin pour les films
    oRequest.addParametersLine(postdata)
    shtml = oRequest.request()

    oParser = cParser()
    sPattern = '<iframe.+?src="([^"]+)"'
    aResult = oParser.parse(shtml, sPattern)
    if (aResult[0] == True):
        sHosterUrl = aResult[1][0]
        # VSlog(sHosterUrl)
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if (oHoster != False):
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()


def showMovieLinks():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sYear = oInputParameterHandler.getValue('sYear')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    cook = oRequestHandler.GetCookies()

    oParser = cParser()
    sPattern = 'property="og:description".+?content="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sDesc = 'FilmoFlix'

    if (aResult[0] == True):
        sDesc = ('[I][COLOR grey]%s[/COLOR][/I] %s') % ('Synopsis :', aResult[1][0])

    sPattern = "lien fx-row.+?\"getxfield.+?(\d+).+?\'([^\']*).+?'([^\']*).+?images.([^\.]+)"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            id = aEntry[0]
            xfield = aEntry[1]
            token = aEntry[2]
            # images :aEntry[3] (VF).png
            hostename = xfield.replace('_', ' ').replace('vf', 'VF')

            sUrl2 = URL_MAIN + 'engine/ajax/getxfield.php?id=' + id + '&xfield=' + xfield + '&token=' + token

            sDisplayTitle = ('%s [COLOR coral]%s[/COLOR]') % (sTitle + ' (' + sYear + ') ', hostename)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('referer', sUrl)
            oOutputParameterHandler.addParameter('cook', cook)
            oGui.addLink(SITE_IDENTIFIER, 'showMovieHosters', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovieHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    referer = oInputParameterHandler.getValue('referer')
    cook = oInputParameterHandler.getValue('cook')

    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('Referer', referer)
    oRequest.addHeaderEntry('Cookie', cook)
    shtml = oRequest.request()

    oParser = cParser()
    sPattern = '<iframe.+?src="([^"]+)"'
    aResult = oParser.parse(shtml, sPattern)

    if (aResult[0] == True):
        sHosterUrl = aResult[1][0]
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if (oHoster != False):
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
