import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractional polynomial basins with non-integer exponents
        fractional_basin = np.sum(0.3 * np.abs(x_norm)**2.7 + 0.4 * np.abs(x_norm)**3.2 + 0.2 * np.abs(x_norm)**1.8)
        
        # Chaotic cross-dimensional coupling using logistic map-like interactions
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for chaos
                chaotic_interaction += np.sin(10 * x_norm[i] * x_norm[j]) * np.cos(7 * x_norm[i] * x_norm[j]) * np.sin(5 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Quantum-like interference patterns with complex sinusoidal combinations
        quantum_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                quantum_interference += np.sin(2 * np.pi * dist) * np.cos(3 * np.pi * dist) * np.exp(-dist**2)
        
        # Multi-scale fractal-like structure with recursive sine components
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += np.sin(12 * np.pi * x_norm[i]) * np.sin(6 * np.pi * x_norm[i]**2) * np.sin(3 * np.pi * x_norm[i]**3)
        
        # Asymmetric saddle with exponential decay and periodic modulation
        asymmetric_saddle = 0.0
        for i in range(self.dim):
            asymmetric_saddle += (x_norm[i]**5) * np.exp(-x_norm[i]**2) * np.cos(4 * np.pi * x_norm[i])
        
        # Cross-dimensional coupling with fractional powers and phase shifts
        cross_fractional = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_fractional += (x_norm[i]**1.5 + x_norm[j]**1.5) * np.sin(2 * np.pi * (x_norm[i] - x_norm[j])) * np.cos(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Add noise and scale the function
        noise = 0.02 * np.random.random()
        
        return 1.5 * fractional_basin + 1.2 * chaotic_interaction + 0.8 * quantum_interference + 0.6 * fractal_component + 0.4 * asymmetric_saddle + 0.3 * cross_fractional + noise