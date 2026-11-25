import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrices for different dimensions
        self.rotations = []
        for i in range(10):  # Precompute up to 10 different rotations
            angle = np.random.rand() * 2 * np.pi
            c, s = np.cos(angle), np.sin(angle)
            self.rotations.append(np.array([[c, -s], [s, c]]))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric chaos component
        chaos = 0
        for i in range(self.dim):
            chaos += np.sin(3 * x[i]) * np.cos(2 * x[i]) + np.tan(0.5 * x[i]) * np.log(np.abs(x[i]) + 1)
        
        # Self-adaptive rotation matrix with dynamic angles
        rot_matrix = np.eye(self.dim)
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                angle = 0.5 * np.sin(x[i] + x[i+1])
                c, s = np.cos(angle), np.sin(angle)
                rot_matrix[i:i+2, i:i+2] = [[c, -s], [s, c]]
        
        # Apply rotation to input vector
        x_rotated = rot_matrix @ x
        
        # Spectral decomposition component with eigenvalue scaling
        spectral = 0
        for i in range(self.dim):
            spectral += (i + 1) * np.sin(2 * x_rotated[i]) * np.cos(3 * x_rotated[i])
        
        # Polynomial coupling with dynamic exponents
        poly_coupling = 0
        for i in range(self.dim):
            exp_val = 2 + 0.5 * np.sin(x[i])
            poly_coupling += (x[i]**exp_val) * np.cos(0.3 * x[i])
        
        # Dynamic condition number via variable scaling
        cond_scale = 1.0
        for i in range(self.dim):
            cond_scale *= (1 + 0.1 * np.abs(x[i]))
        
        # Add noise and global shift
        noise = 0.05 * np.sum(np.random.randn(self.dim) * x)
        shift = 0.2 * np.sum(np.abs(x))
        
        # Combine components with optimized weights
        return cond_scale * (0.5 * chaos + 0.3 * spectral + 0.4 * poly_coupling) + shift + noise