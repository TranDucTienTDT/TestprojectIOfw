
class LoginPageLocators:
    email_txt ="//input[@type='email']"
    password_txt = "//input[@type='password']"
    login_btn = "//button/span[text()='Log in']"
    signup_btn = "//button/span[text()='Sign up']"
    forgot_password_link = "//a[@href='/forgot-password']"


class JobListPageLocators:
    logo_image = "//img[@alt='logo']"
    jobs_image = "//img[@alt='JOBS']"
    candidates_image = "//img[@alt='CANDIDATES']"
    chat_image = "//img[@alt='CHAT']"
    total_credits_balance_lbl = "//span[@class='credit-number']"
    user_avatar = "//div[@id='user-avatar']/img"

    manage_account_dropdownlist_item = "//div[@id='user-dropdown-menu-recruiter']/ul/a"
    logout_dropdownlist_item = "//div[@id='user-dropdown-menu-recruiter']/ul/li"

    post_a_job_btn = "//a[@href='/post-job']/button/span"
    search_job_txt = "//input[@type='text']"
    available_jobmatch_slot_lbl = "//div[text()='Available JobMatch Slot:']/span"

    live_jobs_tag = "//ul/li/span[text()='Live']"
    live_jobs_tag_number = "//ul/li/span[text()='Live']/following-sibling::span[2]"
    paused_jobs_tag = "//ul/li/span[text()='Paused']"
    paused_jobs_tag_number = "//ul/li/span[text()='Paused']/following-sibling::span[2]"
    closed_jobs_tag = "//ul/li/span[text()='Closed']"
    closed_jobs_tag_number = "//ul/li/span[text()='Closed']/following-sibling::span[2]"
    draft_jobs_tag = "//ul/li/span[text()='Draft']"
    draft_jobs_tag_number = "//ul/li/span[text()='Draft']/following-sibling::span[2]"
    all_jobs_tag = "//ul/li/span[text()='All']"
    all_jobs_tag_number = "//ul/li/span[text()='All']/following-sibling::span[2]"

    all_job_types_lbl = "//div/span[text()='All']"


class PostAJobPageLocators:
    public_btn = "//div[@role='button']/div[text()='Public']"
    save_as_draft_btn = "//button/span[text()='Save As Draft']"
    save_n_public_btn = "//button/span[text()='Save & Publish']"
    job_title_txt = "//input[@placeholder='Enter job title']"
    location_txt = ""
    level_dropdownlist = ""
    industry_dropdownlist = ""
    employment_type_dropdownlist = ""
    headcount_txt = ""
    job_desciption_txt = ""
    job_requirement_txt = ""
    paid_leave_chk = ""
    insurance_chk = ""
    bonus_chk = ""
    trainning_chk = ""
    laptop_chk = ""
