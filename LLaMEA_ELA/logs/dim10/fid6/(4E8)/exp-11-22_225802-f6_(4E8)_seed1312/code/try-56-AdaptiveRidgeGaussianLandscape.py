import numpy as np

class AdaptiveRidgeGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        scaled_x = x / 5.0
        
        # Base hyper-elliptic term with adaptive stiffness
        result = np.sum(scaled_x**4)
        
        # Add dynamic Gaussian peaks with varying widths and heights
        peak_penalty = 0.0
        num_peaks = min(10, self.dim)
        for i in range(num_peaks):
            # Adaptive width based on dimension
            width = 0.3 + 0.7 * (i / max(1, self.dim - 1))
            height = 1.5 + 4.0 * (i / max(1, num_peaks - 1))
            
            # Peak position varies with dimension
            peak_pos = np.sin(i * np.pi / max(1, num_peaks)) * 0.9
            
            # Gaussian contribution
            gaussian_term = height * np.exp(-0.5 * ((scaled_x - peak_pos) / width)**2)
            peak_penalty += np.sum(gaussian_term)
            
        result += peak_penalty
        
        # Introduce ridge structures with varying stiffness
        ridge_penalty = 0.0
        for i in range(self.dim):
            # Varying ridge strength based on dimension index
            ridge_strength = 0.3 + 0.7 * (i / max(1, self.dim - 1))
            
            # Ridge term with dynamic scaling
            ridge_term = ridge_strength * np.abs(scaled_x[i])**3.5
            
            # Cross-dimension coupling with neighbor dimensions
            if i > 0:
                ridge_term += 0.3 * np.abs(scaled_x[i] - scaled_x[i-1])**2.5
                
            ridge_penalty += ridge_term
            
        result += ridge_penalty
        
        # Add noise component to increase non-smoothness
        noise = 0.03 * np.sum(np.sin(15 * scaled_x)**2)
        result += noise
        
        # Add cross-dimensional interaction terms
        interaction_penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling between dimensions
                interaction = 0.1 * np.abs(scaled_x[i] - scaled_x[j])**2.2
                interaction_penalty += interaction
                
        result += interaction_penalty
        
        # Global scaling and offset
        result *= (1.0 + 0.15 * self.dim)
        
        return result