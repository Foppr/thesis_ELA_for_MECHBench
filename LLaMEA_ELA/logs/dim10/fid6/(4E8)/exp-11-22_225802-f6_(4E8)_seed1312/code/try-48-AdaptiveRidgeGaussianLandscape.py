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
            width = 0.5 + 0.5 * (i / max(1, self.dim - 1))
            height = 2.0 + 3.0 * (i / max(1, num_peaks - 1))
            
            # Peak position varies with dimension
            peak_pos = np.sin(i * np.pi / max(1, num_peaks)) * 0.8
            
            # Gaussian contribution
            gaussian_term = height * np.exp(-0.5 * ((scaled_x - peak_pos) / width)**2)
            peak_penalty += np.sum(gaussian_term)
            
        result += peak_penalty
        
        # Introduce ridge structures with varying stiffness
        ridge_penalty = 0.0
        for i in range(self.dim):
            # Varying ridge strength based on dimension index
            ridge_strength = 0.5 + 0.5 * (i / max(1, self.dim - 1))
            
            # Ridge term with dynamic scaling
            ridge_term = ridge_strength * np.abs(scaled_x[i])**3
            
            # Cross-dimension coupling with neighbor dimensions
            if i > 0:
                ridge_term += 0.2 * np.abs(scaled_x[i] - scaled_x[i-1])**2
                
            ridge_penalty += ridge_term
            
        result += ridge_penalty
        
        # Add noise component to increase non-smoothness
        noise = 0.05 * np.sum(np.sin(10 * scaled_x)**2)
        result += noise
        
        # Global scaling and offset
        result *= (1.0 + 0.1 * self.dim)
        
        return result