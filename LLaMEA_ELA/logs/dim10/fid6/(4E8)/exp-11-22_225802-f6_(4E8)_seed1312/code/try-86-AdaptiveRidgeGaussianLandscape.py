import numpy as np

class AdaptiveRidgeGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        scaled_x = x / 5.0
        
        # Base hyper-elliptic term with adaptive stiffness
        result = np.sum(scaled_x**6)
        
        # Add dynamic Gaussian peaks with varying widths and heights
        peak_penalty = 0.0
        num_peaks = min(15, self.dim)
        for i in range(num_peaks):
            # Adaptive width based on dimension
            width = 0.2 + 0.8 * (i / max(1, self.dim - 1))
            height = 2.0 + 6.0 * (i / max(1, num_peaks - 1))
            
            # Peak position varies with dimension using chaotic sine
            peak_pos = np.sin(i * np.pi * 1.7 / max(1, num_peaks)) * 0.8
            
            # Gaussian contribution with dynamic exponent (slightly modified)
            gaussian_term = height * np.exp(-0.5 * ((scaled_x - peak_pos) / width)**4.2)
            peak_penalty += np.sum(gaussian_term)
            
        result += peak_penalty
        
        # Introduce ridge structures with varying stiffness and chaotic patterns
        ridge_penalty = 0.0
        for i in range(self.dim):
            # Varying ridge strength based on dimension index with chaotic modulation
            ridge_strength = 0.2 + 0.8 * (i / max(1, self.dim - 1)) * np.sin(i * np.pi * 0.7)
            
            # Ridge term with dynamic scaling and fractional exponent (modified)
            ridge_term = ridge_strength * np.abs(scaled_x[i])**3.8
            
            # Cross-dimension coupling with neighbor dimensions using chaotic weights
            if i > 0:
                coupling_weight = 0.2 + 0.6 * np.sin(i * np.pi * 0.5)
                ridge_term += coupling_weight * np.abs(scaled_x[i] - scaled_x[i-1])**3.5
                
            ridge_penalty += ridge_term
            
        result += ridge_penalty
        
        # Add noise component to increase non-smoothness with chaotic modulation
        noise = 0.05 * np.sum(np.sin(20 * scaled_x)**2.8)
        result += noise
        
        # Add cross-dimensional interaction terms with chaotic coupling (modified coefficients)
        interaction_penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling between dimensions with chaotic modulation
                coupling_mod = 0.2 + 0.3 * np.sin((i+j) * np.pi * 0.4)  # Increased modulation
                interaction = coupling_mod * np.abs(scaled_x[i] - scaled_x[j])**2.5  # Modified exponent
                interaction_penalty += interaction
                
        result += interaction_penalty
        
        # Add nested valley structure with multiple local minima
        nested_penalty = 0.0
        for i in range(self.dim):
            # Nested valleys with varying depths and positions
            valley_depth = 1.0 + 2.0 * np.sin(i * np.pi * 0.4)
            valley_pos = 0.5 * np.cos(i * np.pi * 0.6) * 0.7
            nested_penalty += valley_depth * np.abs(scaled_x[i] - valley_pos)**3.9  # Modified exponent
            
        result += nested_penalty
        
        # Global scaling and offset with chaotic modulation
        global_scale = (1.0 + 0.2 * self.dim) * np.sin(self.dim * 0.3)
        result *= global_scale
        
        return result