import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for harmonic components
        self.harmonic_coeffs = np.array([1.0, 0.7, 0.5, 0.3, 0.2])
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical harmonic component with varying degrees
        r = np.sqrt(np.sum(x_norm**2))
        if r < 1e-10:
            spherical = 0.0
        else:
            # Use a combination of spherical harmonics
            spherical = np.sum(self.harmonic_coeffs * np.sin((np.arange(1, len(self.harmonic_coeffs)+1) + 1) * r))
        
        # Logistic map chaotic dynamics component
        chaotic = 0.0
        for i in range(min(5, self.dim)):  # Limit to first 5 dimensions for chaos
            # Logistic map with parameter 3.9
            if i == 0:
                x_prev = x_norm[i]
            else:
                x_prev = x_norm[i-1]
            chaotic += 3.9 * x_prev * (1 - x_prev)
        
        # Polynomial coupling terms with mixed degrees
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quadratic and cubic coupling
                poly_coupling += 0.1 * (x_norm[i]**2 + x_norm[j]**2) * (x_norm[i] * x_norm[j])
                poly_coupling += 0.05 * (x_norm[i]**3 + x_norm[j]**3)
        
        # Cross-dimensional sinusoidal modulation
        modulation = 0.0
        for i in range(self.dim):
            modulation += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            if i > 0:
                modulation += 0.2 * np.sin(4 * np.pi * x_norm[i-1]) * np.cos(5 * np.pi * x_norm[i])
        
        # Add a global scaling factor and offset
        result = 0.3 * spherical + 0.25 * chaotic + 0.2 * poly_coupling + 0.15 * modulation
        
        # Add a small noise term to break symmetry
        noise = 0.01 * np.random.random()
        
        return result + noise + 1.0