import numpy as np

class ChaoticSinusoidalValleyLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        scaled_x = x / 5.0
        
        # Base hyper-elliptic term with adaptive stiffness
        result = np.sum(scaled_x**8)
        
        # Add nested sinusoidal valleys with varying frequencies and amplitudes
        valley_penalty = 0.0
        num_valleys = min(20, self.dim)
        for i in range(num_valleys):
            # Adaptive frequency and amplitude based on dimension
            freq = 1.0 + 3.0 * (i / max(1, self.dim - 1))
            amp = 1.5 + 4.5 * (i / max(1, num_valleys - 1))
            
            # Valley position with chaotic sine modulation
            valley_pos = np.sin(i * np.pi * 1.618 / max(1, num_valleys)) * 0.9
            
            # Sinusoidal valley contribution with dynamic exponent
            valley_term = amp * np.sin(freq * (scaled_x - valley_pos))**2.5
            valley_penalty += np.sum(valley_term)
            
        result += valley_penalty
        
        # Introduce ridge structures with varying stiffness and chaotic patterns
        ridge_penalty = 0.0
        for i in range(self.dim):
            # Varying ridge strength based on dimension index with chaotic modulation
            ridge_strength = 0.1 + 0.7 * (i / max(1, self.dim - 1)) * np.sin(i * np.pi * 0.8)
            
            # Ridge term with dynamic scaling and fractional exponent
            ridge_term = ridge_strength * np.abs(scaled_x[i])**3.5
            
            # Cross-dimension coupling with neighbor dimensions using chaotic weights
            if i > 0:
                coupling_weight = 0.1 + 0.5 * np.sin(i * np.pi * 0.6)
                ridge_term += coupling_weight * np.abs(scaled_x[i] - scaled_x[i-1])**2.7
                
            ridge_penalty += ridge_term
            
        result += ridge_penalty
        
        # Add noise component to increase non-smoothness with chaotic modulation
        noise = 0.03 * np.sum(np.sin(15 * scaled_x)**3.2)
        result += noise
        
        # Add cross-dimensional interaction terms with chaotic coupling
        interaction_penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling between dimensions with chaotic modulation
                coupling_mod = 0.1 + 0.3 * np.sin((i+j) * np.pi * 0.4)
                interaction = coupling_mod * np.abs(scaled_x[i] - scaled_x[j])**2.3
                interaction_penalty += interaction
                
        result += interaction_penalty
        
        # Add nested valley structure with multiple local minima using sinusoidal modulation
        nested_penalty = 0.0
        for i in range(self.dim):
            # Nested valleys with varying depths and positions using sine modulation
            valley_depth = 1.2 + 2.8 * np.sin(i * np.pi * 0.5)
            valley_pos = 0.6 * np.cos(i * np.pi * 0.7) * 0.8
            nested_penalty += valley_depth * np.abs(scaled_x[i] - valley_pos)**3.9
            
        result += nested_penalty
        
        # Global scaling and offset with chaotic modulation
        global_scale = (1.0 + 0.3 * self.dim) * np.sin(self.dim * 0.4)
        result *= global_scale
        
        return result