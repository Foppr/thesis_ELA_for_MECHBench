import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for the hybrid landscape
        self.basin_strength = 2.0
        self.perturbation_amplitude = 1.5
        self.radial_frequency = 3.0
        self.conditioning_factor = 0.8
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin attraction component
        basin = np.sum(self.basin_strength * (x**2))
        
        # Sinusoidal perturbation with multiple frequencies
        perturbation = 0
        for i in range(self.dim):
            # Multiple frequency components
            freqs = [1.0, 2.0, 3.0, 4.0]
            for f in freqs:
                perturbation += self.perturbation_amplitude * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0)
                
        # Radial symmetry component with varying frequency
        radial = 0
        distance = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            radial += np.sin(self.radial_frequency * distance) * np.exp(-0.1 * (x[i]**2))
            
        # Condition number variation based on dimension and solution proximity
        condition = 0
        for i in range(self.dim):
            # Dynamic conditioning that increases with dimension and distance from origin
            cond_factor = self.conditioning_factor * (1.0 + 0.5 * np.sin(i * np.pi / self.dim))
            condition += cond_factor * (x[i]**4) * np.exp(-0.2 * abs(x[i]))
            
        # Cross-dimensional interaction with varying coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Coupling strength varies with dimension indices
                coupling = 0.5 * (1.0 + np.sin(i * j * 0.5))
                cross += coupling * np.exp(-0.5 * diff**2) * np.cos(3.0 * diff)
                
        # Combine all components
        result = basin + perturbation + radial + condition + cross
        
        # Add dimensionality scaling and offset to ensure positive fitness
        return result + 10.0 * self.dim