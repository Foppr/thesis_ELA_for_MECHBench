import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.delay = 3
        self.adaptation_factor = 0.2
        self.quaternion_weights = np.array([1.0, 1.0j, -1.0, -1.0j])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with quaternion-based scaling
        result = 0.0
        for i in range(self.dim):
            weight = np.abs(self.quaternion_weights[i % 4])
            result += (x[i] ** 2) * (1 + self.adaptation_factor * np.sin(i * 0.7)) * weight
            
        # Chaotic component using quaternion-based delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            delayed_idx = (i - self.delay) % self.dim
            if delayed_idx < 0:
                delayed_idx += self.dim
            # Quaternion-like interaction
            q_interaction = np.sin(x[i] + 0.3 * x[delayed_idx]) * np.cos(1.5 * x[i])
            chaotic_term += q_interaction
            
        # Adaptive frequency modulation with gradient-dependent scaling
        freq_mod = 0.0
        grad_magnitude = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                grad_magnitude += (x[i+1] - x[i])**2
            freq = 3 ** (i % 5) * (1 + 0.4 * np.sin(x[i] * 0.5))
            freq_mod += np.sin(freq * x[i]) * np.cos(freq * x[(i + 3) % self.dim]) * (1 + 0.1 * grad_magnitude)
            
        # Cross-dimensional interaction with quaternion structure
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delayed_i = (i - self.delay) % self.dim
                delayed_j = (j - self.delay) % self.dim
                if delayed_i < 0:
                    delayed_i += self.dim
                if delayed_j < 0:
                    delayed_j += self.dim
                    
                # Quaternion-like cross-term
                q_cross = (x[i] * x[j] + 0.2 * x[delayed_i] * x[delayed_j]) * \
                         np.exp(-0.15 * (x[i] - x[j])**2) * np.sin(4 * (x[i] + x[j]))
                cross_term += q_cross
                
        # Penalty term with dynamic local optima positions
        penalty = 0.0
        for i in range(self.dim):
            # Dynamic shift based on gradient
            shift = 0.5 * np.sin(x[i] * 0.3) * (1 + 0.2 * np.cos(i))
            penalty += ((x[i] - shift)**8 + (x[i] - shift)**6 + (x[i] - shift)**4 + (x[i] - shift)**2) * \
                      (1 + 0.6 * np.cos(i * 0.8))
            
        # Add dynamic fitness scaling based on solution quality
        scale_factor = 1.0 + 0.3 * np.exp(-0.1 * result)
        
        return scale_factor * (result + 0.4 * chaotic_term + 0.25 * freq_mod + 0.2 * cross_term + 0.3 * penalty)