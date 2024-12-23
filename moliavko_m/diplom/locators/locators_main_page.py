import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/'

        super().__init__(web_driver, url)

    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_block_of_video = WebElement(xpath='//section[@class="hero lazy"]')
    vid_hero_video = WebElement(xpath='//video[@class="hero__video"]')
    txt_hero_wrapped_container = WebElement(xpath='//div[@class="hero__wrapper padded container"]')
    txt_hero_text = WebElement(xpath='//h1[@class="h2 hero__title"]')
    btn_video_button = WebElement(xpath='//span[@class="hero__action action--play-video"]')
    txt_video_button_text = WebElement(xpath='(//*[@class="icon icon--play "])[1]')
    btn_video_button_1_play = WebElement(xpath='//span[@class="hero__action action--play"]')
    btn_video_button_1_pause = WebElement(xpath='//span[@class="hero__action action--pause"]')
    btn_video_button_2_mute = WebElement(xpath='//span[@class="hero__action action--mute"]')
    btn_video_button_2_unmute = WebElement(xpath='//span[@class="hero__action action--unmute"]')
    txt_hero_mission = WebElement(xpath='//h2[@class="h4 hero__content-title"]')
    txt_hero_mission_about = WebElement(xpath='//p[@class="hero__content-excerpt"]')
    ###
    txt_ikea_grand = WebElement(xpath='//h1[@class="hero__quote"]')
    txt_ikea_grand_ikea_foundation = WebElement(xpath='(//span[@class="text--green"])[1]')
    txt_ikea_grand_money = WebElement(xpath='(//span[@class="text--green"])[2]')
    txt_ikea_grand_people = WebElement(xpath='(//span[@class="text--green"])[3]')
    txt_ikea_grand_planet = WebElement(xpath='(//span[@class="text--green"])[4]')
    ###
    txt_our_focus = WebElement(xpath='//p[@class="vo-block-paragraph has-black-color has-text-color"]')
    txt_our_focus_people = WebElement(xpath='(//h3[@class="focus__area-header h4"])[1]')
    txt_our_focus_people_text = WebElement(xpath='(//p[@class="focus__area-excerpt"])[1]')
    txt_our_focus_planet = WebElement(xpath='(//h3[@class="focus__area-header h4"])[2]')
    txt_our_focus_planet_text = WebElement(xpath='(//p[@class="focus__area-excerpt"])[2]')
    btn_our_focus_more_button = WebElement(xpath='//a[@class="button"]')
    txt_our_focus_more_button_checking = WebElement(xpath='//p[@class="vo-block-paragraph is-style-lead"]')
    ###
    txt_latest_news = WebElement(xpath='(//h2[@class="border-header"])[2]')
    txt_news_slider = WebElement(xpath='(//div[@class="slider__track"])[1]')
    btn_slider_left_button = WebElement(xpath='(//button[@class="slider__arrow"])[1]')
    btn_slider_right_button = WebElement(xpath='(//button[@class="slider__arrow"])[2]')

    btn_1_news_slide = WebElement(xpath='//div[@id="tns1-item0"]')
    txt_1_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[1]')
    btn_2_news_slide = WebElement(xpath='//div[@id="tns1-item1"]')
    txt_2_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[2]')
    btn_3_news_slide = WebElement(xpath='//div[@id="tns1-item2"]')
    txt_3_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[3]')
    btn_4_news_slide = WebElement(xpath='//div[@id="tns1-item3"]')
    txt_4_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[4]')
    btn_5_news_slide = WebElement(xpath='//div[@id="tns1-item4"]')
    txt_5_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[5]')
    btn_6_news_slide = WebElement(xpath='//div[@id="tns1-item5"]')
    txt_6_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[6]')
    btn_7_news_slide = WebElement(xpath='//div[@id="tns1-item6"]')
    txt_7_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[7]')
    btn_8_news_slide = WebElement(xpath='//div[@id="tns1-item7"]')
    txt_8_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[8]')
    btn_9_news_slide = WebElement(xpath='//div[@id="tns1-item8"]')
    txt_9_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[9]')
    btn_10_news_slide = WebElement(xpath='//div[@id="tns1-item9"]')
    txt_10_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[10]')
    btn_11_news_slide = WebElement(xpath='//div[@id="tns1-item10"]')
    txt_11_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[11]')
    btn_12_news_slide = WebElement(xpath='//div[@id="tns1-item11"]')
    txt_12_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[12]')
    btn_13_news_slide = WebElement(xpath='//div[@id="tns1-item12"]')
    txt_13_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[13]')
    btn_14_news_slide = WebElement(xpath='//div[@id="tns1-item13"]')
    txt_14_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[14]')
    btn_15_news_slide = WebElement(xpath='//div[@id="tns1-item14"]')
    txt_15_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[15]')
    btn_16_news_slide = WebElement(xpath='//div[@id="tns1-item15"]')
    txt_16_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[16]')
    btn_17_news_slide = WebElement(xpath='//div[@id="tns1-item16"]')
    txt_17_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[17]')
    btn_18_news_slide = WebElement(xpath='//div[@id="tns1-item17"]')
    txt_18_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[18]')
    btn_19_news_slide = WebElement(xpath='//div[@id="tns1-item18"]')
    txt_19_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[19]')
    btn_20_news_slide = WebElement(xpath='//div[@id="tns1-item19"]')
    txt_20_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[20]')
    btn_21_news_slide = WebElement(xpath='//div[@id="tns1-item20"]')
    txt_21_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[21]')
    btn_22_news_slide = WebElement(xpath='//div[@id="tns1-item21"]')
    txt_22_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[22]')
    btn_23_news_slide = WebElement(xpath='//div[@id="tns1-item22"]')
    txt_23_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[23]')
    btn_24_news_slide = WebElement(xpath='//div[@id="tns1-item23"]')
    txt_24_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[24]')
    btn_25_news_slide = WebElement(xpath='//div[@id="tns1-item24"]')
    txt_25_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[25]')
    btn_26_news_slide = WebElement(xpath='//div[@id="tns1-item25"]')
    txt_26_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[26]')
    btn_27_news_slide = WebElement(xpath='//div[@id="tns1-item26"]')
    txt_27_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[27]')
    btn_28_news_slide = WebElement(xpath='//div[@id="tns1-item27"]')
    txt_28_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[28]')
    btn_29_news_slide = WebElement(xpath='//div[@id="tns1-item28"]')
    txt_29_news_slide_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[29]')
    ###
    txt_citates_slider = WebElement(xpath='(//div[@class="slider__track"])[2]')
    btn_citates_slider_left_button = WebElement(xpath='(//button[@class="slider__arrow"])[3]')
    btn_citates_slider_right_button = WebElement(xpath='(//button[@class="slider__arrow"])[4]')


    txt_1_slide_citates_block = WebElement(xpath='//div[@id="tns2-item0"]')
    txt_1_slide_citate_text = WebElement(xpath='(//div[@class="quote-card__title h3"])[1]')
    txt_1_slide_autor = WebElement(xpath='(//p[@class="quote-card__author"])[1]')

    txt_2_slide_citates_block = WebElement(xpath='//div[@id="tns2-item1"]')
    txt_2_slide_citate_text = WebElement(xpath='(//div[@class="quote-card__title h3"])[2]')
    txt_2_slide_autor = WebElement(xpath='(//p[@class="quote-card__author"])[2]')

    txt_3_slide_citates_block = WebElement(xpath='//div[@id="tns2-item2"]')
    txt_3_slide_citate_text = WebElement(xpath='(//div[@class="quote-card__title h3"])[3]')
    txt_3_slide_autor = WebElement(xpath='(//p[@class="quote-card__author"])[3]')

    txt_4_slide_citates_block = WebElement(xpath='//div[@id="tns2-item3"]')
    txt_4_slide_citate_text = WebElement(xpath='(//div[@class="quote-card__title h3"])[4]')
    txt_4_slide_autor = WebElement(xpath='(//p[@class="quote-card__author"])[4]')

    txt_5_slide_citates_block = WebElement(xpath='//div[@id="tns2-item4"]')
    txt_5_slide_citate_text = WebElement(xpath='(//div[@class="quote-card__title h3"])[5]')
    txt_5_slide_autor = WebElement(xpath='(//p[@class="quote-card__author"])[5]')

    txt_6_slide_citates_block = WebElement(xpath='//div[@id="tns2-item5"]')
    txt_6_slide_citate_text = WebElement(xpath='(//div[@class="quote-card__title h3"])[6]')
    txt_6_slide_autor = WebElement(xpath='(//p[@class="quote-card__author"])[6]')
    ###
    txt_our_grands = WebElement(xpath='(//h2[@class="border-header"])[3]')
    txt_our_grands_text = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[1]')
    btn_our_grands_more_buttons = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[1]')
    txt_our_grands_more_button_checking = WebElement(xpath='//p[@class="archive-page__description h4"]')
    txt_our_learnings = WebElement(xpath='(//h2[@class="border-header"])[4]')
    txt_our_learnings_text = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[2]')
    btn_our_learnings_more_button = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[2]')
    txt_our_learnings_more_button_checking = WebElement(xpath='//div[@class="archive-page__description h4"]')
    txt_partners_block = WebElement(xpath='//div[@class="partner-grid"]')
    txt_partners_cards = ManyWebElements(xpath='//div[@class="partner-grid__card"]')
    txt_partners_block_about = WebElement(xpath='//div[@class="partner-block"]')
    txt_partners_block_about_text = WebElement(xpath='//h3[@class="border-header h2"]')
    txt_partners_block_about_text_text = WebElement(xpath='//p[@class="partner-block__excerpt"]')
    btn_partners_block_more_about_partners_button = WebElement(xpath='//a[@class="link link--white"]')
    btn_learn_about_our_work_together_button = WebElement(xpath='//a[@class="link"]')
