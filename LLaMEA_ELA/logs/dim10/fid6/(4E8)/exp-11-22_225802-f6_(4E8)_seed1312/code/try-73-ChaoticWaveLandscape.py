import numpy as np

class ChaoticWaveLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        scaled_x = x / 5.0
        
        # Base exponential decay term
        result = np.sum(np.exp(-scaled_x**2))
        
        # Add trigonometric wave interactions with varying frequencies
        wave_penalty = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * (i / max(1, self.dim - 1))
            wave_term = np.sin(freq * scaled_x[i]) * np.cos(freq * scaled_x[i])
            wave_penalty += wave_term
            
        result += 0.5 * wave_penalty
        
        # Introduce adaptive conditioning with exponential scaling
        condition_penalty = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 3.0 * np.exp(-0.5 * (i / max(1, self.dim - 1))**2)
            condition_term = cond_factor * scaled_x[i]**4
            condition_penalty += condition_term
            
        result += condition_penalty
        
        # Add chaotic cross-dimensional coupling using logarithmic interactions
        log_penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    log_interaction = np.log(1.0 + np.abs(scaled_x[i] - scaled_x[j]))
                    log_penalty += log_interaction
                    
        result += 0.3 * log_penalty
        
        # Include sharp transition regions with piecewise exponential functions
        transition_penalty = 0.0
        for i in range(self.dim):
            if scaled_x[i] < -0.5:
                transition_penalty += np.exp(-scaled_x[i]**2) * 0.8
            elif scaled_x[i] > 0.5:
                transition_penalty += np.exp(scaled_x[i]**2) * 0.8
            else:
                transition_penalty += 0.1 * scaled_x[i]**6
                
        result += transition_penalty
        
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.2 * self.dim)
        
        return result