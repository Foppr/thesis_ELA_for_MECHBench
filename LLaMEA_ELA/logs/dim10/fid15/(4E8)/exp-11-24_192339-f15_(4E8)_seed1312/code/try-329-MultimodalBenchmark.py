import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        self.d = 0.8
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spatiotemporal chaotic dynamics component
        chaotic_dyn = 0
        for i in range(self.dim):
            # Time-varying chaotic map with adaptive parameters
            param_a = self.a + 0.1 * np.sin(0.3 * x[i] + self.dim * 0.2)
            param_b = self.b + 0.05 * np.cos(0.4 * x[i] + self.dim * 0.15)
            
            # Logistic-like chaotic term
            chaotic_dyn += param_a * x[i] * (1 - x[i]**2) * np.exp(-param_b * x[i]**2)
        
        # Multi-scale fractal interference pattern
        fractal_pattern = 0
        for i in range(self.dim):
            scale1 = 1.5 + 0.3 * np.sin(0.7 * x[i] + self.dim * 0.4)
            scale2 = 2.0 + 0.4 * np.cos(0.5 * x[i] + self.dim * 0.3)
            fractal_pattern += np.sin(scale1 * x[i]) * np.cos(scale2 * x[i]**3) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive basin stability component
        basin_stability = 0
        for i in range(self.dim):
            # Basin depth varies with dimension and input
            depth = 1.2 + 0.3 * np.sin(0.6 * x[i] + self.dim * 0.25)
            basin_stability += depth * (x[i]**4 - 2 * x[i]**2) * np.exp(-0.15 * x[i]**2)
        
        # Cross-dimensional coupling with variable interaction strength
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Adaptive coupling coefficient based on input values
                coupling_strength = 0.8 + 0.2 * np.sin(0.5 * (x[i] + x[j]) + self.dim * 0.1)
                cross_coupling += coupling_strength * np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
        
        # Multi-modal trigonometric structure with dynamic frequency
        multimodal_structure = 0
        for i in range(self.dim):
            freq1 = 2.5 + 0.5 * np.sin(0.8 * x[i] + self.dim * 0.3)
            freq2 = 3.0 + 0.4 * np.cos(0.6 * x[i] + self.dim * 0.2)
            multimodal_structure += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]**2) + \
                                  np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]**3)
        
        # Final landscape combining all components
        return (0.3 * chaotic_dyn + 0.25 * fractal_pattern + 
                0.2 * basin_stability + 0.15 * cross_coupling + 0.1 * multimodal_structure)