import numpy as np

class ChaoticQuantumInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        
        # Chaotic tent map parameters for each dimension
        self.tent_r = np.random.uniform(1.5, 3.9, dim)
        self.tent_offset = np.random.uniform(-1.0, 1.0, dim)
        
        # Quantum-like interference parameters
        self.interference_amplitude = np.random.uniform(0.5, 2.5, dim)
        self.interference_phase = np.random.uniform(0, 2*np.pi, dim)
        self.interference_frequency = np.random.uniform(1.0, 8.0, dim)
        
        # Evolutionary pressure gradients
        self.pressure_magnitude = np.random.uniform(0.1, 1.5, dim)
        self.pressure_direction = np.random.randn(dim)
        self.pressure_direction /= np.linalg.norm(self.pressure_direction)
        
        # Emergent symmetry breaking parameters
        self.symmetry_breaking_strength = np.random.uniform(0.3, 1.2, dim)
        self.symmetry_breaking_frequency = np.random.uniform(0.5, 3.0, dim)
        
        # Fitness valley sharpness parameters
        self.valley_depth = np.random.uniform(1.0, 5.0, dim)
        self.valley_width = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic tent map dynamics
        for i in range(self.dim):
            tent_value = x[i]
            for _ in range(10):  # Iterate chaotic map
                if tent_value < 0.5:
                    tent_value = self.tent_r[i] * tent_value
                else:
                    tent_value = self.tent_r[i] * (1 - tent_value)
            result += 0.3 * np.abs(tent_value - self.tent_offset[i])
        
        # Quantum-like interference patterns
        for i in range(self.dim):
            interference = self.interference_amplitude[i] * np.sin(
                self.interference_frequency[i] * x[i] + self.interference_phase[i]
            )
            result += 0.4 * np.abs(interference)**2
        
        # Evolutionary pressure gradients
        pressure_gradient = np.dot(x, self.pressure_direction) * self.pressure_magnitude
        result += 0.5 * np.abs(pressure_gradient)
        
        # Emergent symmetry breaking
        for i in range(self.dim):
            symmetry_break = self.symmetry_breaking_strength[i] * np.sin(
                self.symmetry_breaking_frequency[i] * x[i]
            )
            result += 0.2 * np.abs(symmetry_break)**3
        
        # Fitness valleys with sharp transitions
        for i in range(self.dim):
            valley_term = self.valley_depth[i] * np.exp(-0.5 * ((x[i] - np.sin(i)) / self.valley_width[i])**2)
            result += 0.6 * valley_term
            
        # Add global multimodality through polynomial coupling
        poly_coupling = np.sum(np.sin(3 * x)**3) + 0.1 * np.sum(x**4)
        result += 0.3 * np.abs(poly_coupling)
        
        return result