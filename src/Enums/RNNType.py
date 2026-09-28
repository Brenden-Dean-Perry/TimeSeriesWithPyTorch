from enum import Enum


class RNNType(Enum):
    SimpleRNN = 0,
    """
    Simple RNN is a type of recurrent neural network.
    
    How It Works
    
    - Sequence processing: It handles data point by point across time steps.
    - Hidden state: At every step, the RNN takes the current input and the previous hidden state (memory) to calculate a new hidden state.
    - Looping connection: This loop allows past information to influence current and future predictions.
    
    Key Limitations
    
    - Short memory: It struggles to remember information over long sequences.
    - Vanishing gradients: As data moves through many steps, the mathematical signals can become too small, stopping the network from learning effectively.
    
    """
    LSTM = 1,
    """
    Long Short-Term Memory is a type of recurrent neural network designed to process sequential data and remember 
    long-term dependencies.
    
    LSTMs solve this by introducing a cell state (long-term memory) and a hidden state (short-term memory), managed 
    by three main gates:
    
    - Forget Gate: Decides what old information to throw away from the cell state using a value between 0 and 1.
    - Input Gate: Determines what new information to add to the cell state
    - Output Gate: Controls what data from the updated cell state becomes the next hidden state and output.
    
    Advantages: Effectively retains context over long text or time steps; prevents gradients from vanishing or exploding; 
    performs well on smaller or noisy datasets compared to transformers.
    
    """
    GRU = 2
    """
    Gated Recurrent Unit is a type of recurrent neural network  (RNN) introduced in 2014 that solves the vanishing 
    gradient problem using fewer parameters than an LSTM.
    
    How GRU Works
    - Update Gate: Decides how much past information from previous hidden states needs to be carried forward into the future.
    - Reset Gate: Determines how much of the past hidden state to forget or ignore when building a new candidate state.
    - Single Hidden State: Combines both short-term and long-term memory into one hidden state, omitting the separate cell state found in LSTMs.
    
    Speed: GRUs train faster and use less memory because they have fewer parameters and a lower computational load.
    Accuracy: LSTMs can be more accurate on extremely long sequences, while GRUs perform similarly on many standard text, speech, and time-series tasks.
    """