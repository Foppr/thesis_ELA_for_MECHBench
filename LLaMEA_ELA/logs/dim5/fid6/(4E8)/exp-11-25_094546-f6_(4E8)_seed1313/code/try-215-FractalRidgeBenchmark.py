import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal ridge structure with self-similar patterns - increased frequency
            ridge = 0.0
            for k in range(1, 8):  # Extended range for more complexity
                scale = 2.0 ** (-k)
                freq = 3 ** k  # Increased base frequency
                ridge += scale * np.sin(freq * xi) * np.cos(freq * xi)
            
            # Adaptive curvature field with dimension-dependent scaling
            curvature = 1.0 + 0.7 * np.sin(self.dim * 0.25 + i * 0.35) * np.cos(i * 0.45)  # Increased amplitude
            
            # Cross-dimensional coupling with fractal interaction - modified strength
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Modified interaction strength
                    interaction_strength = 1.5 / (1.0 + distance**2.5)  # Increased coupling influence
                    coupling += interaction_strength * np.sin(xi + x_norm[j] + 0.6 * np.cos(i + j))  # Shifted phase
            
            # Multi-scale harmonic modulation - altered scaling
            modulation = 1.0
            for k in range(1, 5):  # Extended range
                modulation *= (1.0 + 0.4 * np.sin(k * xi + k * 0.25))  # Increased modulation
            
            # Add to result with adaptive weighting - modified weights
            weight = 1.0 + 0.5 * np.sin(i * 0.55) * np.cos(self.dim * 0.12 + i)  # Changed frequency
            
            # Apply chaotic amplification - altered chaos
            chaos_amp = 1.0 + 0.4 * np.sin(np.sum(x_norm**2) + i * 0.25)  # Increased chaos
            
            result += weight * chaos_amp * (curvature * ridge**2 + 0.6 * coupling)**2  # Increased coupling factor
            
        # Global fractal scaling with dimension-dependent correction - modified scaling
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 5.0)  # Increased scaling
        
        # Add hyper-fractal modulation based on all dimensions - altered modulation
        hyper_fractal = 1.0 + 0.25 * np.sin(np.sum(np.abs(x_norm)) * 3.5 + self.dim * 0.35)  # Increased modulation
        
        return global_scale * hyper_fractal * result / self.dim