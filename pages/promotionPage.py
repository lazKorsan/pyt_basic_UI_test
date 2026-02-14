# promotionPage.py
class PromotionPage:
    MARKETINGBUTTON_XPATH = '//*[@href="#marketingCollapse"]'
    GOLDPROMOTIONS_XPATH = '//button[@data-promotion-id="2"]'
    SELECTCOURSEOPTIONS_XPATH = '(//select[@name="webinar_id"])[2]'
    COURSE_OPTION_XPATH = '//option[@value="3662"]'
    PAYBUTTON_XPATH = '(//button[@class="btn btn-sm btn-primary js-submit-promotion"])[2]'
