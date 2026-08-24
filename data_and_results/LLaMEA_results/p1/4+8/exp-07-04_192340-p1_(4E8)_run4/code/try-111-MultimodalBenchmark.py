import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for rotation-invariance
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Normalize rotation matrix
        self.rotation = self.rotation / (np.linalg.norm(self.rotation) + 1e-8)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Add a scaling factor for modulating the landscape complexity
        self.scaling = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function
        result = 0.0
        for i in range(self.dim):
            # Polynomial term with varying degree and scaling
            poly_term = (x_rot[i] ** (i + 2)) * self.scaling[i] * 0.1
            result += poly_term
            
            # Trigonometric components with varying frequencies
            trig_term = np.sin(x_rot[i] * (i + 1) * np.pi) * np.cos(x_rot[i] * (i + 1) * np.pi / 2)
            result += trig_term * self.scaling[i] * 0.2
            
            # Exponentially modulated sinusoidal term to create ruggedness
            exp_mod = np.exp(-0.5 * x_rot[i] ** 2) * np.sin(x_rot[i] * np.pi * (i + 1) * 2)
            result += exp_mod * self.scaling[i] * 0.15
            
            # Additional nested multimodal component
            nested = np.sin(x_rot[i] * np.pi * (i + 1) * 4) * np.cos(x_rot[i] * np.pi * (i + 1) * 3)
            result += nested * self.scaling[i] * 0.1
            
            # Log barrier to keep values in check
            log_barrier = np.log(1 + np.abs(x_rot[i]) ** 2) * 0.05
            result += log_barrier
        
        # Add a global penalty term to encourage convergence to the global minimum
        penalty = 0.01 * np.sum(np.abs(x_rot) ** 3)
        result += penalty
        
        return result