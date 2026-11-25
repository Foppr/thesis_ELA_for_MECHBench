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
            width = 0.3 + 0.7 * (i / max(1, self.dim - 1))
            height = 1.0 + 4.0 * (i / max(1, num_peaks - 1))
            
            # Peak position varies with dimension using chaotic mapping
            peak_pos = np.sin(i * np.pi * 1.618) * 0.9
            
            # Gaussian contribution
            gaussian_term = height * np.exp(-0.5 * ((scaled_x - peak_pos) / width)**2)
            peak_penalty += np.sum(gaussian_term)
            
        result += peak_penalty
        
        # Introduce ridge structures with varying stiffness and chaotic coupling
        ridge_penalty = 0.0
        for i in range(self.dim):
            # Varying ridge strength based on dimension index with sinusoidal modulation
            ridge_strength = 0.3 + 0.7 * np.sin(i * np.pi / max(1, self.dim)) * 0.5
            
            # Ridge term with dynamic scaling and chaotic factor
            ridge_term = ridge_strength * np.abs(scaled_x[i])**4
            
            # Cross-dimension coupling with neighbor dimensions using chaotic weights
            if i > 0:
                coupling_weight = 0.3 + 0.7 * np.sin(i * np.pi * 0.618)
                ridge_term += coupling_weight * np.abs(scaled_x[i] - scaled_x[i-1])**3
                
            ridge_penalty += ridge_term
            
        result += ridge_penalty
        
        # Add chaotic sinusoidal noise component
        noise = 0.1 * np.sum(np.sin(15 * scaled_x) * np.cos(7 * scaled_x))
        result += noise
        
        # Add nested multimodal structure with multiple scales
        nested_penalty = 0.0
        for i in range(self.dim):
            nested_penalty += 2.0 * np.sin(scaled_x[i] * 10) * np.cos(scaled_x[i] * 3)
            
        result += nested_penalty
        
        # Global scaling and offset
        result *= (1.0 + 0.2 * self.dim)
        
        return result