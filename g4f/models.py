from __future__  import annotations

from dataclasses import dataclass

from .Provider import IterListProvider, ProviderType
from .Provider import (
    ### No Auth Required ###
    ARTA,
    Blackbox,
    Chatai,
    ChatGLM,
    Cloudflare,
    Copilot,
    DDG,
    DeepInfraChat,
    DocsBot,
    Dynaspark,
    Free2GPT,
    FreeGpt,
    HarProvider,
    HuggingSpace,
    Grok,
    DeepseekAI_JanusPro7b,
    DeepSeekAPI,
    ImageLabs,
    LambdaChat,
    Liaobots,
    OIVSCodeSer2,
    OIVSCodeSer5,
    OIVSCodeSer0501,
    OpenAIFM,
    PerplexityLabs,
    Pi,
    PollinationsAI,
    PollinationsImage,
    TeachAnything,
    Websim,
    WeWordle,
    Yqcloud,
    Microsoft_Phi_4_Multimodal,
    
    ### Needs Auth ###
    BingCreateImages,
    CopilotAccount,
    Gemini,
    GeminiPro,
    HailuoAI,
    HuggingChat,
    HuggingFace,
    HuggingFaceAPI,
    MetaAI,
    MicrosoftDesigner,
    OpenaiAccount,
    OpenaiChat,
    Reka,
)

@dataclass(unsafe_hash=True)
class Model:
    """
    Represents a machine learning model configuration.

    Attributes:
        name (str): Name of the model.
        base_provider (str): Default provider for the model.
        best_provider (ProviderType): The preferred provider for the model, typically with retry logic.
    """
    name: str
    base_provider: str
    best_provider: ProviderType = None

    @staticmethod
    def __all__() -> list[str]:
        """Returns a list of all model names."""
        return _all_models

class ImageModel(Model):
    pass

class AudioModel(Model):
    pass
    
class VideoModel(Model):
    pass
    
class VisionModel(Model):
    pass

### Default ###
default = Model(
    name = "",
    base_provider = "",
    best_provider = IterListProvider([
        Blackbox,
        DDG,
        Copilot,
        OIVSCodeSer2,
        OIVSCodeSer5,
        OIVSCodeSer0501,
        DeepInfraChat,
        LambdaChat,
        PollinationsAI,
        Free2GPT,
        FreeGpt,
        Dynaspark,
        Chatai,
        WeWordle,
        DocsBot,
        OpenaiChat,
        Cloudflare,
    ])
)

default_vision = VisionModel(
    name = "",
    base_provider = "",
    best_provider = IterListProvider([
        Blackbox,
        DeepInfraChat,
        OIVSCodeSer2,
        OIVSCodeSer5,
        OIVSCodeSer0501,
        PollinationsAI,
        Dynaspark,
        DocsBot,
        HuggingSpace,
        GeminiPro,
        HuggingFaceAPI,
        CopilotAccount,
        OpenaiAccount,
        Gemini,
    ], shuffle=False)
)

##########################
### Text//Audio/Vision ###
##########################

### OpenAI ###
# gpt-3.5
gpt_3_5_turbo = Model(
    name          = 'gpt-3.5-turbo',
    base_provider = 'OpenAI',
    best_provider = HarProvider
)

# gpt-4
gpt_4 = Model(
    name          = 'gpt-4',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, DDG, PollinationsAI, Copilot, Yqcloud, WeWordle, Liaobots, OpenaiChat])
)

gpt_4_turbo = Model(
    name          = 'gpt-4-turbo',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Liaobots])
)

# gpt-4o
gpt_4o = VisionModel(
    name          = 'gpt-4o',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, PollinationsAI, DocsBot, OpenaiChat])
)

gpt_4o_mini = Model(
    name          = 'gpt-4o-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, DDG, OIVSCodeSer2, PollinationsAI, Chatai, Liaobots, OpenaiChat])
)

gpt_4o_mini_audio = AudioModel(
    name          = 'gpt-4o-mini-audio',
    base_provider = 'OpenAI',
    best_provider = PollinationsAI
)

gpt_4o_mini_tts = AudioModel(
    name          = 'gpt-4o-mini-tts',
    base_provider = 'OpenAI',
    best_provider = OpenAIFM
)

# o1
o1 = Model(
    name          = 'o1',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Copilot, OpenaiAccount])
)

o1_mini = Model(
    name          = 'o1-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([OpenaiAccount])
)

# o3
o3_mini = Model(
    name          = 'o3-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, Blackbox, Liaobots])
)

o3_mini_high = Model(
    name          = 'o3-mini-high',
    base_provider = 'OpenAI',
    best_provider = OpenaiChat
)

# o4
o4_mini = Model(
    name          = 'o4-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([PollinationsAI, OpenaiChat])
)

o4_mini_high = Model(
    name          = 'o4-mini-high',
    base_provider = 'OpenAI',
    best_provider = OpenaiChat
)

# gpt-4.1
gpt_4_1 = Model(
    name          = 'gpt-4.1',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([PollinationsAI, OpenaiChat, Liaobots])
)

gpt_4_1_mini = Model(
    name          = 'gpt-4.1-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([OIVSCodeSer5, OIVSCodeSer0501, PollinationsAI, Liaobots])
)

gpt_4_1_nano = Model(
    name          = 'gpt-4.1-nano',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, PollinationsAI])
)

gpt_4_5 = Model(
    name          = 'gpt-4.5',
    base_provider = 'OpenAI',
    best_provider = OpenaiChat
)

# dall-e
dall_e_3 = ImageModel(
    name = 'dall-e-3',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([PollinationsImage, CopilotAccount, OpenaiAccount, MicrosoftDesigner, BingCreateImages])
)

### Meta ###
meta = Model(
    name          = "meta-ai",
    base_provider = "Meta",
    best_provider = MetaAI
)

# llama 2
llama_2_7b = Model(
    name          = "llama-2-7b",
    base_provider = "Meta Llama",
    best_provider = Cloudflare
)

# llama-3
llama_3_8b = Model(
    name          = "llama-3-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Cloudflare])
)

# llama-3.1
llama_3_1_8b = Model(
    name          = "llama-3.1-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox, DeepInfraChat, Cloudflare])
)

# llama-3.2
llama_3_2_1b = Model(
    name          = "llama-3.2-1b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox, Cloudflare])
)

llama_3_2_3b = Model(
    name          = "llama-3.2-3b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox])
)

llama_3_2_11b = VisionModel(
    name          = "llama-3.2-11b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox, HuggingChat])
)

llama_3_2_90b = Model(
    name          = "llama-3.2-90b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DeepInfraChat])
)

# llama-3.3
llama_3_3_70b = Model(
    name          = "llama-3.3-70b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox, DDG, DeepInfraChat, LambdaChat, PollinationsAI])
)

# llama-4
llama_4_scout = Model(
    name          = "llama-4-scout",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox, PollinationsAI, Cloudflare])
)

llama_4_scout_17b = Model(
    name          = "llama-4-scout-17b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DeepInfraChat, PollinationsAI])
)

llama_4_maverick = Model(
    name          = "llama-4-maverick",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox, DeepInfraChat])
)

llama_4_maverick_17b = Model(
    name          = "llama-4-maverick-17b",
    base_provider = "Meta Llama",
    best_provider = DeepInfraChat
)

### MistralAI ###
mistral_7b = Model(
    name          = "mistral-7b",
    base_provider = "Mistral AI",
    best_provider = IterListProvider([Blackbox])
)

mixtral_8x22b = Model(
    name          = "mixtral-8x22b",
    base_provider = "Mistral AI",
    best_provider = IterListProvider([DeepInfraChat])
)

mistral_nemo = Model(
    name          = "mistral-nemo",
    base_provider = "Mistral AI",
    best_provider = IterListProvider([Blackbox, HuggingChat, HuggingFace])
)

mistral_small = Model(
    name          = "mistral-small",
    base_provider = "Mistral AI",
    best_provider = IterListProvider([Blackbox, DDG, DeepInfraChat])
)

mistral_small_24b = Model(
    name          = "mistral-small-24b",
    base_provider = "Mistral AI",
    best_provider = IterListProvider([Blackbox, DDG, DeepInfraChat])
)

mistral_small_3_1_24b = Model(
    name          = "mistral-small-3.1-24b",
    base_provider = "Mistral AI",
    best_provider = IterListProvider([Blackbox, PollinationsAI])
)

### NousResearch ###

hermes_3_405b = Model(
    name          = "hermes-3-405b",
    base_provider = "NousResearch",
    best_provider = IterListProvider([LambdaChat])
)

# deephermes-3
deephermes_3_8b = Model(
    name          = "deephermes-3-8b",
    base_provider = "NousResearch",
    best_provider = IterListProvider([Blackbox])
)

### Microsoft ###
# phi-3
phi_3_5_mini = Model(
    name          = "phi-3.5-mini",
    base_provider = "Microsoft",
    best_provider = IterListProvider([HuggingFace, HuggingChat])
)

# phi-4
phi_4 = Model(
    name          = "phi-4",
    base_provider = "Microsoft",
    best_provider = IterListProvider([DeepInfraChat, PollinationsAI, HuggingSpace])
)

phi_4_multimodal = VisionModel(
    name          = "phi-4-multimodal",
    base_provider = "Microsoft",
    best_provider = IterListProvider([DeepInfraChat, Microsoft_Phi_4_Multimodal, HuggingSpace])
)

phi_4_reasoning = Model(
    name          = "phi-4-reasoning",
    base_provider = "Microsoft",
    best_provider = IterListProvider([DeepInfraChat])
)

phi_4_reasoning_plus = Model(
    name          = "phi-4-reasoning-plus",
    base_provider = "Microsoft",
    best_provider = IterListProvider([DeepInfraChat])
)


# wizardlm
wizardlm_2_7b = Model(
    name = 'wizardlm-2-7b',
    base_provider = 'Microsoft',
    best_provider = DeepInfraChat
)

wizardlm_2_8x22b = Model(
    name = 'wizardlm-2-8x22b',
    base_provider = 'Microsoft',
    best_provider = IterListProvider([DeepInfraChat])
)

### Google DeepMind ###
# gemini
gemini = Model(
    name          = 'gemini-2.0',
    base_provider = 'Google',
    best_provider = Gemini
)

# gemini-1.0
gemini_1_0_pro = Model(
    name          = 'gemini-1.0-pro',
    base_provider = 'Google',
    best_provider = Liaobots
)

# gemini-1.5
gemini_1_5_flash = Model(
    name          = 'gemini-1.5-flash',
    base_provider = 'Google',
    best_provider = IterListProvider([Free2GPT, FreeGpt, TeachAnything, Websim, Dynaspark, GeminiPro])
)

gemini_1_5_pro = Model(
    name          = 'gemini-1.5-pro',
    base_provider = 'Google',
    best_provider = IterListProvider([Free2GPT, FreeGpt, TeachAnything, Websim, GeminiPro])
)

# gemini-2.0
gemini_2_0_flash = Model(
    name          = 'gemini-2.0-flash',
    base_provider = 'Google',
    best_provider = IterListProvider([Blackbox, Dynaspark, Liaobots, GeminiPro, Gemini])
)

gemini_2_0_flash_thinking = Model(
    name          = 'gemini-2.0-flash-thinking',
    base_provider = 'Google',
    best_provider = IterListProvider([PollinationsAI, Liaobots, Gemini])
)

gemini_2_0_flash_thinking_with_apps = Model(
    name          = 'gemini-2.0-flash-thinking-with-apps',
    base_provider = 'Google',
    best_provider = Gemini
)

# gemini-2.5
gemini_2_5_flash = Model(
    name          = 'gemini-2.5-flash',
    base_provider = 'Google',
    best_provider = IterListProvider([PollinationsAI, Gemini])
)

gemini_2_5_pro = Model(
    name          = 'gemini-2.5-pro',
    base_provider = 'Google',
    best_provider = IterListProvider([Gemini])
)

# gemma-2
gemma_2_9b = Model(
    name          = 'gemma-2-9b',
    base_provider = 'Google',
    best_provider = IterListProvider([Blackbox])
)

# gemma-3
gemma_3_1b = Model(
    name          = 'gemma-3-1b',
    base_provider = 'Google',
    best_provider = IterListProvider([Blackbox])
)

gemma_3_4b = Model(
    name          = 'gemma-3-4b',
    base_provider = 'Google',
    best_provider = IterListProvider([Blackbox])
)

gemma_3_12b = Model(
    name          = 'gemma-3-12b',
    base_provider = 'Google',
    best_provider = IterListProvider([Blackbox, DeepInfraChat])
)

gemma_3_27b = Model(
    name          = 'gemma-3-27b',
    base_provider = 'Google',
    best_provider = IterListProvider([Blackbox, DeepInfraChat])
)

### Anthropic ###
# claude 3

claude_3_haiku = Model(
    name          = 'claude-3-haiku',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([DDG])
)

# claude 3.5
claude_3_5_sonnet = Model(
    name          = 'claude-3.5-sonnet',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([Blackbox, Liaobots])
)

# claude 3.7
claude_3_7_sonnet = Model(
    name          = 'claude-3.7-sonnet',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([Blackbox, Liaobots])
)

### Reka AI ###
reka_core = Model(
    name = 'reka-core',
    base_provider = 'Reka AI',
    best_provider = Reka
)

reka_flash = Model(
    name = 'reka-flash',
    base_provider = 'Reka AI',
    best_provider = IterListProvider([Blackbox])
)

### Blackbox AI ###
blackboxai = Model(
    name = 'blackboxai',
    base_provider = 'Blackbox AI',
    best_provider = Blackbox
)

command_r = Model(
    name = 'command-r',
    base_provider = 'CohereForAI',
    best_provider = IterListProvider([HuggingSpace])
)

command_r_plus = Model(
    name = 'command-r-plus',
    base_provider = 'CohereForAI',
    best_provider = IterListProvider([HuggingSpace, HuggingChat])
)

command_r7b = Model(
    name = 'command-r7b',
    base_provider = 'CohereForAI',
    best_provider = IterListProvider([HuggingSpace])
)

command_a = Model(
    name = 'command-a',
    base_provider = 'CohereForAI',
    best_provider = IterListProvider([HuggingSpace])
)

### Qwen ###
# qwen-1.5
qwen_1_5_7b = Model(
    name = 'qwen-1.5-7b',
    base_provider = 'Qwen',
    best_provider = Cloudflare
)

# qwen-2
qwen_2_72b = Model(
    name = 'qwen-2-72b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([DeepInfraChat, HuggingSpace])
)
qwen_2_vl_7b = VisionModel(
    name = "qwen-2-vl-7b",
    base_provider = 'Qwen',
    best_provider = HuggingFaceAPI
)

# qwen-2.5
qwen_2_5 = Model(
    name = 'qwen-2.5',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

qwen_2_5_7b = Model(
    name = 'qwen-2.5-7b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox])
)

qwen_2_5_72b = Model(
    name = 'qwen-2.5-72b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox])
)

qwen_2_5_coder_32b = Model(
    name = 'qwen-2.5-coder-32b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox, PollinationsAI, LambdaChat, HuggingChat])
)

qwen_2_5_1m = Model(
    name = 'qwen-2.5-1m',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

qwen_2_5_max = Model(
    name = 'qwen-2-5-max',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

qwen_2_5_vl_3b = Model(
    name = 'qwen-2.5-vl-3b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox])
)

qwen_2_5_vl_7b = Model(
    name = 'qwen-2.5-vl-7b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox])
)

qwen_2_5_vl_32b = Model(
    name = 'qwen-2.5-vl-32b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox])
)

qwen_2_5_vl_72b = Model(
    name = 'qwen-2.5-vl-72b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox])
)

# qwen3
qwen_3_235b = Model(
    name = 'qwen-3-235b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([DeepInfraChat, HuggingSpace, Liaobots])
)

qwen_3_32b = Model(
    name = 'qwen-3-32b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([DeepInfraChat, HuggingSpace])
)

qwen_3_30b = Model(
    name = 'qwen-3-30b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([DeepInfraChat, HuggingSpace])
)

qwen_3_14b = Model(
    name = 'qwen-3-14b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([DeepInfraChat, HuggingSpace])
)

qwen_3_4b = Model(
    name = 'qwen-3-4b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([HuggingSpace])
)

qwen_3_1_7b = Model(
    name = 'qwen-3-1.7b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([HuggingSpace])
)

qwen_3_0_6b = Model(
    name = 'qwen-3-0.6b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([HuggingSpace])
)

### qwq/qvq ###
qwq_32b = Model(
    name = 'qwq-32b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Blackbox, DeepInfraChat, PollinationsAI, HuggingChat])
)

qwq_32b_preview = Model(
    name = 'qwq-32b-preview',
    base_provider = 'Qwen',
    best_provider = Blackbox
)

qwq_32b_arliai = Model(
    name = 'qwq-32b-arliai',
    base_provider = 'Qwen',
    best_provider = Blackbox
)

qvq_72b = VisionModel(
    name = 'qvq-72b',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

### Inflection ###
pi = Model(
    name = 'pi',
    base_provider = 'Inflection',
    best_provider = Pi
)

### DeepSeek ###
# deepseek
deepseek_chat = Model(
    name = 'deepseek-chat',
    base_provider = 'DeepSeek',
    best_provider = DeepSeekAPI
)

# deepseek-v3
deepseek_v3 = Model(
    name = 'deepseek-v3',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([DeepInfraChat, PollinationsAI, Liaobots])
)

# deepseek-r1
deepseek_r1 = Model(
    name = 'deepseek-r1',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox, DeepInfraChat, LambdaChat, PollinationsAI, HuggingChat, HuggingFace])
)

deepseek_r1_zero = Model(
    name = 'deepseek-r1-zero',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox])
)

deepseek_r1_turbo = Model(
    name = 'deepseek-r1-turbo',
    base_provider = 'DeepSeek',
    best_provider = DeepInfraChat
)

deepseek_r1_distill_llama_70b = Model(
    name = 'deepseek-r1-distill-llama-70b',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox, DeepInfraChat, PollinationsAI])
)

deepseek_r1_distill_qwen_14b = Model(
    name = 'deepseek-r1-distill-qwen-14b',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox])
)

deepseek_r1_distill_qwen_32b = Model(
    name = 'deepseek-r1-distill-qwen-32b',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox, DeepInfraChat, PollinationsAI])
)

# deepseek-v2
deepseek_prover_v2 = Model(
    name = 'deepseek-prover-v2',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([DeepInfraChat])
)

deepseek_prover_v2_671b = Model(
    name = 'deepseek-prover-v2-671b',
    base_provider = 'DeepSeek',
    best_provider = DeepInfraChat
)

# deepseek-v3-0324
deepseek_v3_0324 = Model(
    name = 'deepseek-v3-0324',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([DeepInfraChat, PollinationsAI])
)

# janus
janus_pro_7b = VisionModel(
    name = DeepseekAI_JanusPro7b.default_model,
    base_provider = 'DeepSeek',
    best_provider = DeepseekAI_JanusPro7b
)

### x.ai ###
grok_2 = Model(
    name = 'grok-2',
    base_provider = 'x.ai',
    best_provider = IterListProvider([Grok, Liaobots])
)

grok_3 = Model(
    name = 'grok-3',
    base_provider = 'x.ai',
    best_provider = IterListProvider([Grok, Liaobots])
)

grok_3_r1 = Model(
    name = 'grok-3-r1',
    base_provider = 'x.ai',
    best_provider = Grok
)

grok_3_reason = Model(
    name = 'grok-3-reason',
    base_provider = 'x.ai',
    best_provider = Liaobots
)

### Perplexity AI ### 
sonar = Model(
    name = 'sonar',
    base_provider = 'Perplexity AI',
    best_provider = IterListProvider([PerplexityLabs])
)

sonar_pro = Model(
    name = 'sonar-pro',
    base_provider = 'Perplexity AI',
    best_provider = IterListProvider([PerplexityLabs])
)

sonar_reasoning = Model(
    name = 'sonar-reasoning',
    base_provider = 'Perplexity AI',
    best_provider = IterListProvider([PerplexityLabs])
)

sonar_reasoning_pro = Model(
    name = 'sonar-reasoning-pro',
    base_provider = 'Perplexity AI',
    best_provider = IterListProvider([PerplexityLabs])
)

r1_1776 = Model(
    name = 'r1-1776',
    base_provider = 'Perplexity AI',
    best_provider = IterListProvider([PerplexityLabs])
)

### Nvidia ### 
nemotron_49b = Model(
    name = 'nemotron-49b',
    base_provider = 'Nvidia',
    best_provider = IterListProvider([Blackbox])
)

nemotron_70b = Model(
    name = 'nemotron-70b',
    base_provider = 'Nvidia',
    best_provider = IterListProvider([LambdaChat, HuggingChat, HuggingFace])
)

nemotron_253b = Model(
    name = 'nemotron-253b',
    base_provider = 'Nvidia',
    best_provider = IterListProvider([Blackbox])
)

### THUDM ### 
glm_4 = Model(
    name = 'glm-4',
    base_provider = 'THUDM',
    best_provider = IterListProvider([ChatGLM])
)

### MiniMax ###
mini_max = Model(
    name = "minimax",
    base_provider = "MiniMax",
    best_provider = IterListProvider([HailuoAI])
)

### Cognitive Computations ###
# dolphin-2
dolphin_2_6 = Model(
    name = "dolphin-2.6",
    base_provider = "Cognitive Computations",
    best_provider = DeepInfraChat
)

dolphin_2_9 = Model(
    name = "dolphin-2.9",
    base_provider = "Cognitive Computations",
    best_provider = DeepInfraChat
)

# dolphin-3
dolphin_3_0_24b = Model(
    name = "dolphin-3.0-24b",
    base_provider = "Cognitive Computations",
    best_provider = IterListProvider([Blackbox])
)

dolphin_3_0_r1_24b = Model(
    name = "dolphin-3.0-r1-24b",
    base_provider = "Cognitive Computations",
    best_provider = IterListProvider([Blackbox])
)

### DeepInfra ###
airoboros_70b = Model(
    name = "airoboros-70b",
    base_provider = "DeepInfra",
    best_provider = DeepInfraChat
)

### Lizpreciatior ###
lzlv_70b = Model(
    name = "lzlv-70b",
    base_provider = "Lizpreciatior",
    best_provider = DeepInfraChat
)

### Ai2 ###
molmo_7b = Model(
    name = "molmo-7b",
    base_provider = "Ai2",
    best_provider = Blackbox
)

lfm_40b = Model(
    name = "lfm-40b",
    base_provider = "Liquid AI",
    best_provider = IterListProvider([LambdaChat])
)

### Agentica ###
deepcode_14b = Model(
    name = "deepcoder-14b",
    base_provider = "Agentica",
    best_provider = IterListProvider([Blackbox])
)

### Moonshot AI ###
kimi_vl_thinking = Model(
    name = "kimi-vl-thinking",
    base_provider = "Moonshot AI",
    best_provider = IterListProvider([Blackbox])
)

moonlight_16b = Model(
    name = "moonlight-16b",
    base_provider = "Moonshot AI",
    best_provider = IterListProvider([Blackbox])
)

### Featherless Serverless LLM ### 
qwerky_72b = Model(
    name = 'qwerky-72b',
    base_provider = 'Featherless Serverless LLM',
    best_provider = IterListProvider([Blackbox])
)

### Uncensored AI ### 
evil = Model(
    name = 'evil',
    base_provider = 'Evil Mode - Experimental',
    best_provider = PollinationsAI
)

### Stability AI ###
sdxl_turbo = ImageModel(
    name = 'sdxl-turbo',
    base_provider = 'Stability AI',
    best_provider = IterListProvider([PollinationsImage, ImageLabs])
)

sd_3_5 = ImageModel(
    name = 'stable-diffusion-3.5-large',
    base_provider = 'Stability AI',
    best_provider = HuggingSpace
)

### Black Forest Labs ###
flux = ImageModel(
    name = 'flux',
    base_provider = 'Black Forest Labs',
    best_provider = IterListProvider([PollinationsImage, Websim, HuggingSpace, ARTA])
)

flux_pro = ImageModel(
    name = 'flux-pro',
    base_provider = 'Black Forest Labs',
    best_provider = PollinationsImage
)

flux_dev = ImageModel(
    name = 'flux-dev',
    base_provider = 'Black Forest Labs',
    best_provider = IterListProvider([PollinationsImage, HuggingSpace, HuggingChat, HuggingFace])
)

flux_schnell = ImageModel(
    name = 'flux-schnell',
    base_provider = 'Black Forest Labs',
    best_provider = IterListProvider([PollinationsImage, HuggingSpace, HuggingChat, HuggingFace])
)

### Midjourney ###
midjourney = ImageModel(
    name = 'midjourney',
    base_provider = 'Midjourney',
    best_provider = PollinationsImage
)

class ModelUtils:
    """
    Utility class for mapping string identifiers to Model instances.

    Attributes:
        convert (dict[str, Model]): Dictionary mapping model string identifiers to Model instances.
    """
    convert: dict[str, Model] = { 
        ### OpenAI ###       
        # gpt-3.5
        gpt_3_5_turbo.name: gpt_3_5_turbo,
        
        # gpt-4
        gpt_4.name: gpt_4,
        gpt_4_turbo.name: gpt_4_turbo,
        
        # gpt-4o
        gpt_4o.name: gpt_4o,
        gpt_4o_mini.name: gpt_4o_mini,
        gpt_4o_mini_audio.name: gpt_4o_mini_audio,
        gpt_4o_mini_tts.name: gpt_4o_mini_tts,
        
        # o1
        o1.name: o1,
        o1_mini.name: o1_mini,
        
        # o3
        o3_mini.name: o3_mini,
        o3_mini_high.name: o3_mini_high,
        
        # o4
        o4_mini.name: o4_mini,
        o4_mini_high.name: o4_mini_high,

        # gpt-4.1
        gpt_4_1.name: gpt_4_1,
        gpt_4_1_nano.name: gpt_4_1_nano,
        gpt_4_1_mini.name: gpt_4_1_mini,
        
        # gpt-4.5
        gpt_4_5.name: gpt_4_5,
        
        # dall-e
        dall_e_3.name: dall_e_3,

        ### Meta ###
        meta.name: meta,

        # llama-2
        llama_2_7b.name: llama_2_7b,

        # llama-3
        llama_3_8b.name: llama_3_8b,
                
        # llama-3.1
        llama_3_1_8b.name: llama_3_1_8b,
        # llama-3.2
        llama_3_2_1b.name: llama_3_2_1b,
        llama_3_2_3b.name: llama_3_2_3b,
        llama_3_2_11b.name: llama_3_2_11b,
        llama_3_2_90b.name: llama_3_2_90b,
        
        # llama-3.3
        llama_3_3_70b.name: llama_3_3_70b,

        # llama-4
        llama_4_scout.name: llama_4_scout,
        llama_4_scout_17b.name: llama_4_scout_17b,
        llama_4_maverick.name: llama_4_maverick,
        llama_4_maverick_17b.name: llama_4_maverick_17b,
                
        ### Mistral ###
        mistral_7b.name: mistral_7b,
        mixtral_8x22b.name: mixtral_8x22b,
        mistral_nemo.name: mistral_nemo,
        mistral_small.name: mistral_small,
        mistral_small_24b.name: mistral_small_24b,
        mistral_small_3_1_24b.name: mistral_small_3_1_24b,

        ### NousResearch ###
        hermes_3_405b.name: hermes_3_405b,
        
         # deephermes-3
        deephermes_3_8b.name: deephermes_3_8b,
                
        ### Microsoft ###
        # phi-3
        phi_3_5_mini.name: phi_3_5_mini,
        
        # phi-4
        phi_4.name: phi_4,
        phi_4_multimodal.name: phi_4_multimodal,
        phi_4_reasoning_plus.name: phi_4_reasoning_plus,
        
        # wizardlm
        wizardlm_2_7b.name: wizardlm_2_7b,
        wizardlm_2_8x22b.name: wizardlm_2_8x22b,

        ### Google ###
        ### gemini
        "gemini": gemini,
        gemini.name: gemini,
        
        # gemini-1.0
        gemini_1_0_pro.name: gemini_1_0_pro,
        
        # gemini-1.5
        gemini_1_5_pro.name: gemini_1_5_pro,
        gemini_1_5_flash.name: gemini_1_5_flash,
        
        # gemini-2.0
        gemini_2_0_flash.name: gemini_2_0_flash,
        gemini_2_0_flash_thinking.name: gemini_2_0_flash_thinking,
        gemini_2_0_flash_thinking_with_apps.name: gemini_2_0_flash_thinking_with_apps,
        
        # gemini-2.5
        gemini_2_5_flash.name: gemini_2_5_flash,
        gemini_2_5_pro.name: gemini_2_5_pro,
        
        # gemma-2
        gemma_2_9b.name: gemma_2_9b,
        # gemma-3
        gemma_3_12b.name: gemma_3_12b,
        gemma_3_1b.name: gemma_3_1b,
        gemma_3_27b.name: gemma_3_27b,
        gemma_3_4b.name: gemma_3_4b,

        ### Anthropic ###
        
        # claude 3
        claude_3_haiku.name: claude_3_haiku,
        
        # claude 3.5
        claude_3_5_sonnet.name: claude_3_5_sonnet,
        
        # claude 3.7
        claude_3_7_sonnet.name: claude_3_7_sonnet,

        ### Reka AI ###
        reka_core.name: reka_core,
        reka_flash.name: reka_flash,

        ### Blackbox AI ###
        blackboxai.name: blackboxai,

        ### CohereForAI ###
        command_r.name: command_r,
        command_r_plus.name: command_r_plus,
        command_r7b.name: command_r7b,
        command_a.name: command_a,

        ### Qwen ###
        # qwen-1.5
        qwen_1_5_7b.name: qwen_1_5_7b,
        
        # qwen-2
        qwen_2_72b.name: qwen_2_72b,
        qwen_2_vl_7b.name: qwen_2_vl_7b,
        
        # qwen-2.5
        qwen_2_5.name: qwen_2_5,
        qwen_2_5_7b.name: qwen_2_5_7b,
        qwen_2_5_72b.name: qwen_2_5_72b,
        qwen_2_5_coder_32b.name: qwen_2_5_coder_32b,
        qwen_2_5_1m.name: qwen_2_5_1m,
        qwen_2_5_max.name: qwen_2_5_max,
        qwen_2_5_vl_3b.name: qwen_2_5_vl_3b,
        qwen_2_5_vl_7b.name: qwen_2_5_vl_7b,
        qwen_2_5_vl_32b.name: qwen_2_5_vl_32b,
        qwen_2_5_vl_72b.name: qwen_2_5_vl_72b,
        
        # qwen-3
        qwen_3_235b.name: qwen_3_235b,
        qwen_3_32b.name: qwen_3_32b,
        qwen_3_30b.name: qwen_3_30b,
        qwen_3_14b.name: qwen_3_14b,
        qwen_3_4b.name: qwen_3_4b,
        qwen_3_1_7b.name: qwen_3_1_7b,
        qwen_3_0_6b.name: qwen_3_0_6b,

        # qwq/qvq
        qwq_32b.name: qwq_32b,
        qwq_32b_preview.name: qwq_32b_preview,
        qwq_32b_arliai.name: qwq_32b_arliai,
        qvq_72b.name: qvq_72b,

        ### Inflection ###
        pi.name: pi,

        ### x.ai ###
        grok_3.name: grok_3,
        grok_3_r1.name: grok_3_r1,
        grok_3_reason.name: grok_3_reason,

        ### Perplexity AI ###
        sonar.name: sonar,
        sonar_pro.name: sonar_pro,
        sonar_reasoning.name: sonar_reasoning,
        sonar_reasoning_pro.name: sonar_reasoning_pro,
        r1_1776.name: r1_1776,

        ### DeepSeek ###       
        # deepseek
        deepseek_chat.name: deepseek_chat,
        
        # deepseek-v3
        deepseek_v3.name: deepseek_v3,
        
        # deepseek-r1
        deepseek_r1.name: deepseek_r1,
        deepseek_r1_zero.name: deepseek_r1_zero,
        deepseek_r1_turbo.name: deepseek_r1_turbo,
        deepseek_r1_distill_qwen_14b.name: deepseek_r1_distill_qwen_14b,
        deepseek_r1_distill_qwen_32b.name: deepseek_r1_distill_qwen_32b,
        
        # deepseek-v2
        deepseek_prover_v2_671b.name: deepseek_prover_v2_671b,
        
        # deepseek-v3-0324
        deepseek_v3_0324.name: deepseek_v3_0324,

        ### Nvidia ###
        nemotron_49b.name: nemotron_49b,
        nemotron_70b.name: nemotron_70b,
        nemotron_253b.name: nemotron_253b,
        
        ### THUDM ###
        glm_4.name: glm_4,
        
        ### MiniMax ###
        mini_max.name: mini_max, 
        
        ### Cognitive Computations ###
        # dolphin-2
        dolphin_2_6.name: dolphin_2_6,
        dolphin_2_9.name: dolphin_2_9,
        
        # dolphin-3
        dolphin_3_0_24b.name: dolphin_3_0_24b,
        dolphin_3_0_r1_24b.name: dolphin_3_0_r1_24b,
        
        ### DeepInfra ###
        airoboros_70b.name: airoboros_70b,
        
        ### Lizpreciatior ###
        lzlv_70b.name: lzlv_70b,

        ### Ai2 ###
        molmo_7b.name: molmo_7b,
        
        ### Liquid AI ###
        lfm_40b.name: lfm_40b,
        
        ### Agentica ###
        deepcode_14b.name: deepcode_14b,
        
        ### Moonshot AI ###
        kimi_vl_thinking.name: kimi_vl_thinking,
        moonlight_16b.name: moonlight_16b,
        
        ### Featherless Serverless LLM ###
        qwerky_72b.name: qwerky_72b,
        
        ### Uncensored AI ###
        evil.name: evil,

        ### Stability AI ###
        sdxl_turbo.name: sdxl_turbo,
        sd_3_5.name: sd_3_5,

        ### Flux AI ###
        flux.name: flux,
        flux_pro.name: flux_pro,
        flux_dev.name: flux_dev,
        flux_schnell.name: flux_schnell,
        
        ### Midjourney ###
        midjourney.name: midjourney,
    }

demo_models = {
    llama_3_2_11b.name: [llama_3_2_11b, [HuggingChat]],
    qwen_2_vl_7b.name: [qwen_2_vl_7b, [HuggingFaceAPI]],
    deepseek_r1.name: [deepseek_r1, [HuggingFace, PollinationsAI]],
    janus_pro_7b.name: [janus_pro_7b, [HuggingSpace]],
    command_r.name: [command_r, [HuggingSpace]],
    command_r_plus.name: [command_r_plus, [HuggingSpace]],
    command_r7b.name: [command_r7b, [HuggingSpace]],
    qwen_2_5_coder_32b.name: [qwen_2_5_coder_32b, [HuggingFace]],
    qwq_32b.name: [qwq_32b, [HuggingFace]],
    llama_3_3_70b.name: [llama_3_3_70b, [HuggingFace]],
    sd_3_5.name: [sd_3_5, [HuggingSpace, HuggingFace]],
    flux_dev.name: [flux_dev, [PollinationsImage, HuggingFace, HuggingSpace]],
    flux_schnell.name: [flux_schnell, [PollinationsImage, HuggingFace, HuggingSpace]],
}

# Create a list of all models and his providers
__models__  = {
    model.name: (model, providers)
        for model, providers in [
            (model, [provider for provider in model.best_provider.providers if provider.working]
                if isinstance(model.best_provider, IterListProvider)
                else [model.best_provider]
                if model.best_provider is not None and model.best_provider.working
                else [])
        for model in ModelUtils.convert.values()]
        if model.name and [True for provider in providers if provider.working]
    }
_all_models = list(__models__.keys())
