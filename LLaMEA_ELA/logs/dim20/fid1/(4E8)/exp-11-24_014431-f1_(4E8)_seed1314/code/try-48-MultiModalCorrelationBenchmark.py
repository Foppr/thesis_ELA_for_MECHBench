import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sine-wave correlation structure with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction based on sine waves with exponential modulation
                freq = np.exp(0.1 * (i + j))
                amp = 0.3 * np.sin(0.7 * i) * np.cos(0.5 * j)
                corr = amp * np.sin(freq * (x[i] - x[j])) * np.cos(freq * (x[i] + x[j]))
                f_val += corr
        
        # Add highly multimodal sinusoidal terms with chaotic frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 2.5 + 0.5 * np.sin(0.3 * i)
            freq2 = 4.0 + 0.8 * np.cos(0.4 * i)
            amp1 = 0.6 + 0.2 * np.sin(0.6 * i)
            amp2 = 0.4 + 0.3 * np.cos(0.5 * i)
            f_val += amp1 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + \
                     amp2 * np.sin(freq1 * x[i] ** 2) * np.cos(freq2 * x[i] ** 2)
            
        # Add adaptive polynomial conditioning with exponential penalties
        for i in range(self.dim):
            # Exponentially varying degrees and coefficients
            degree = 3 + int(2 * np.sin(0.2 * i))
            coeff = 0.05 * (1 + 0.5 * np.cos(0.3 * i))
            f_val += coeff * x[i] ** degree
            
        # Add cross-dimensional exponential interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential modulation based on dimension indices
                mod = np.exp(-0.2 * (i + j)) * np.sin(0.8 * (i - j))
                f_val += 0.3 * mod * np.exp(x[i] * x[j])
                
        # Add chaotic global modulation with multiple sine components
        global_mod = 0.5 * np.sin(np.sum(x) * 0.3) + \
                     0.3 * np.cos(np.sum(x) * 0.7) + \
                     0.2 * np.sin(np.sum(x) * 1.1)
        f_val += global_mod
        
        # Add noise-like perturbations to increase ruggedness
        for i in range(self.dim):
            f_val += 0.03 * np.sin(10 * x[i]) * np.cos(8 * x[i])
            
        return f_val