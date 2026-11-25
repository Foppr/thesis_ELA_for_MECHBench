import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for conditioning
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Apply rotation for conditioning
        x_rot = self.rotation_matrix @ x_norm
        
        # Dynamic conditioning: varying condition numbers per dimension
        condition_numbers = 10 ** (np.linspace(0, 3, self.dim))
        
        # Quadratic base with dynamic conditioning
        quadratic = np.sum(condition_numbers * x_rot**2)
        
        # Chaotic sine modulation with multi-scale frequencies
        chaotic_mod = 0.0
        for i in range(self.dim):
            freqs = [1, 3, 7, 11, 19]
            for f in freqs:
                chaotic_mod += np.sin(f * x_rot[i]) * np.cos(f * x_rot[i] / (f + 1))
        
        # Asymmetric elliptic components with rotation-dependent coupling
        elliptic = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            elliptic += (x_rot[i]**2 + 0.3 * x_rot[j]**2) * np.sin(2 * x_rot[i]) * np.cos(2 * x_rot[j])
        
        # Hybrid gradient structure with exponential and polynomial components
        hybrid_grad = 0.0
        for i in range(self.dim):
            hybrid_grad += (np.exp(-x_rot[i]**2) * np.sin(5 * x_rot[i]) + 
                           0.1 * x_rot[i]**3 * np.cos(3 * x_rot[i]))
        
        # Multi-scale harmonic interference with dynamic amplitude
        interference = 0.0
        for i in range(self.dim):
            amp = 1.0 / (1.0 + np.exp(-x_rot[i]))
            interference += amp * np.sin(20 * x_rot[i]) * np.cos(15 * x_rot[i])
        
        # Cross-dimensional coupling with nonlinear interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x_rot[i] * x_rot[j])**2 * np.sin(x_rot[i] + x_rot[j])
        
        # Fractal-like basin structure with self-similar modulations
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(100 * x_rot[i]) * np.cos(50 * x_rot[i]) + \
                       0.5 * np.sin(200 * x_rot[i])**2
        
        # Combine all components with adaptive weights based on dimension
        weights = np.linspace(1.0, 0.2, self.dim)
        total = (quadratic * 0.3 + 
                chaotic_mod * 0.25 + 
                elliptic * 0.15 + 
                hybrid_grad * 0.15 + 
                interference * 0.1 + 
                coupling * 0.05 + 
                fractal * 0.05)
        
        return total