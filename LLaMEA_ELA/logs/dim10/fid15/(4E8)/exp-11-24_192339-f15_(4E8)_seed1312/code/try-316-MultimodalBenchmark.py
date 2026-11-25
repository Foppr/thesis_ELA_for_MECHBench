import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic weights for stability
        self.weights = np.random.uniform(0.5, 2.0, dim)
        self.biases = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic neural network layer with dynamic weights
        neural_output = 0
        for i in range(self.dim):
            # Dynamic weight modulation based on input and chaotic phase
            mod_weight = self.weights[i] * (1 + 0.3 * np.sin(x[i] * 2.0 + i * 0.5))
            # Activation function with chaotic feedback
            act = np.tanh(mod_weight * x[i] + self.biases[i])
            neural_output += act * np.exp(-0.1 * x[i]**2)
        
        # Temporal recurrent coupling with memory effect
        recurrent_term = 0
        for i in range(self.dim):
            # Coupling with previous dimensions (temporal memory)
            if i > 0:
                coupling = 0.2 * np.sin(x[i-1] + x[i]) * np.cos(0.5 * x[i])
                recurrent_term += coupling
        
        # Multi-scale fractal topology with exponential scaling
        fractal_term = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(2.0 * x[i] + i * 0.3)
            fractal_term += scale * np.exp(-0.2 * (x[i]**2)) * np.cos(3.0 * x[i])
        
        # Adaptive conditioning with dynamic exponent
        condition_factor = 1.5 + 0.4 * np.sin(self.dim * 0.7 + np.sum(x) * 0.1)
        
        # Cross-dimensional interaction with non-linear coupling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j]))
                cross_interaction += interaction
        
        # Asymmetric multimodal component with chaotic modulation
        asym_term = 0
        for i in range(self.dim):
            mod_freq = 2.0 + 1.0 * np.cos(x[i] * 0.5 + i * 0.2)
            asym_term += np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i]**3) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with optimized weights
        return condition_factor * (0.3 * neural_output + 
                                  0.25 * recurrent_term + 
                                  0.2 * fractal_term + 
                                  0.15 * cross_interaction + 
                                  0.1 * asym_term)