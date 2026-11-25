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
        
        # Quantum-inspired superposition component with phase modulation
        quantum_superposition = 0
        for i in range(self.dim):
            phase = 0.5 * np.sin(1.2 * x[i] + self.dim * 0.3) + 0.3 * np.cos(0.8 * x[i] + self.dim * 0.2)
            amplitude = 1.5 + 0.5 * np.sin(0.6 * x[i] + self.dim * 0.4)
            quantum_superposition += amplitude * np.sin(x[i] + phase) * np.cos(x[i] - phase)
        
        # Time-varying chaotic attractor with adaptive parameters
        chaotic_attractor = 0
        for i in range(self.dim):
            param_a = self.a + 0.2 * np.sin(0.4 * x[i] + self.dim * 0.25)
            param_b = self.b + 0.1 * np.cos(0.3 * x[i] + self.dim * 0.2)
            param_c = self.c + 0.05 * np.sin(0.5 * x[i] + self.dim * 0.15)
            
            # Modified logistic map with adaptive coupling
            chaotic_attractor += param_a * x[i] * (1 - x[i]**2) * np.exp(-param_b * x[i]**2) + \
                                param_c * np.sin(x[i]) * np.cos(0.5 * x[i])
        
        # Multi-scale fractal interference pattern with dynamic scaling
        fractal_pattern = 0
        for i in range(self.dim):
            scale1 = 1.8 + 0.4 * np.sin(0.6 * x[i] + self.dim * 0.35)
            scale2 = 2.2 + 0.3 * np.cos(0.4 * x[i] + self.dim * 0.25)
            fractal_pattern += np.sin(scale1 * x[i]) * np.cos(scale2 * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive ridge structures with varying curvature
        ridge_structure = 0
        for i in range(self.dim):
            curvature = 1.0 + 0.4 * np.sin(0.7 * x[i] + self.dim * 0.3)
            ridge_structure += curvature * (x[i]**4 - 2 * x[i]**2) * np.exp(-0.2 * x[i]**2)
        
        # Cross-dimensional coupling with dynamic interaction
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Dynamic coupling coefficient based on input values and dimension
                coupling_strength = 0.9 + 0.1 * np.sin(0.6 * (x[i] + x[j]) + self.dim * 0.2)
                cross_coupling += coupling_strength * np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
        
        # Multi-modal trigonometric structure with quantum frequency modulation
        multimodal_structure = 0
        for i in range(self.dim):
            freq1 = 2.8 + 0.6 * np.sin(0.7 * x[i] + self.dim * 0.3)
            freq2 = 3.2 + 0.5 * np.cos(0.5 * x[i] + self.dim * 0.2)
            multimodal_structure += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]**2) + 
                                  np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]**3)) * \
                                 np.exp(-0.15 * x[i]**2)
        
        # Final landscape combining all components with enhanced weighting
        return (0.25 * quantum_superposition + 0.3 * chaotic_attractor + 
                0.15 * fractal_pattern + 0.15 * ridge_structure + 
                0.1 * cross_coupling + 0.05 * multimodal_structure)