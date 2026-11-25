import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for chaos induction
        np.random.seed(42)
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to induce non-separability
        x_rot = self.rotation_matrix @ x
        
        # Composite sinusoidal potential with varying frequencies and amplitudes
        potential = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * x_rot[i] + i * 0.2)
            amp = 1.0 + 0.3 * np.cos(0.4 * x_rot[i] + i * 0.1)
            potential += amp * np.sin(freq * x_rot[i]) * np.exp(-0.1 * x_rot[i]**2)
        
        # Adaptive conditioning based on dimensionality
        condition = 1.0 + 0.5 * np.sin(self.dim * 0.1)
        
        # Saddle-point structure with exponential decay
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_rot[i]**2 - 1.0)**2 * np.exp(-0.5 * x_rot[i]**2)
        
        # Multi-scale oscillatory component
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(2.0 * x_rot[i]) * np.cos(3.0 * x_rot[i]) * np.sin(5.0 * x_rot[i])
        
        # Chaotic modulation factor
        chaos_factor = 1.0 + 0.2 * np.sin(np.sum(x_rot) * 0.5)
        
        # Combine all components with dynamic weights
        return condition * (0.4 * potential + 0.3 * saddle + 
                           0.2 * oscillatory + 0.1 * chaos_factor)