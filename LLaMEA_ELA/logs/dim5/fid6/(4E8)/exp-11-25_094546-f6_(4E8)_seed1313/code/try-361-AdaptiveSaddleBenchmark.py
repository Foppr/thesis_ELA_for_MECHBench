import numpy as np

class AdaptiveSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced asymmetric quadratic basin with chaotic curvature
            curvature = 1.0 + 0.7 * np.sin(self.dim * 0.3 + i * 0.4) + 0.5 * np.cos(self.dim * 0.2 + i * 0.5)
            basin = 0.6 * curvature * xi**2
            
            # Quantum-inspired saddle point with entanglement coupling
            saddle_strength = 1.0 + 0.5 * np.sin(i * 0.6 + self.dim * 0.4)
            saddle = saddle_strength * xi * np.cos(4 * xi) * np.exp(-0.3 * xi**2) * np.sin(self.dim * 0.2 + i * 0.3)
            
            # Complex asymmetric cubic term with fractal-like behavior
            asymmetry = 0.4 * np.sin(i * 0.8 + self.dim * 0.3)
            cubic = (1.0 + asymmetry) * xi**3
            
            # Fractal multimodal component with quantum interference patterns
            freq_factor = 1.2 + 0.6 * np.cos(self.dim * 0.15 + i * 0.25)
            modal_term = 0.7 * freq_factor * np.sin(7 * xi + i * 0.4)**2 * np.cos(3 * xi + self.dim * 0.2)
            
            # Cross-dimensional interaction with quantum entanglement coupling
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling += 0.15 * np.sin(xi + x_norm[j] + 0.3 * i) * np.cos(3 * xi - x_norm[j] + 0.15 * j) * np.exp(-0.2 * abs(xi - x_norm[j]))
            
            # Dimensionally adaptive scaling factor with chaotic modulation
            scale_factor = 1.0 + 0.4 * np.sin(self.dim * 0.5 + i * 0.3) + 0.2 * np.cos(self.dim * 0.4 + i * 0.2)
            
            # Add all components to the result
            result += scale_factor * (basin + saddle + cubic + modal_term + coupling)
        
        # Global adaptive correction with chaotic resonance terms
        global_correction = 1.0 + 0.3 * np.sin(self.dim * 0.4) + 0.2 * np.cos(self.dim * 0.3) + 0.1 * np.sin(self.dim * 0.6)
        
        return global_correction * result / self.dim