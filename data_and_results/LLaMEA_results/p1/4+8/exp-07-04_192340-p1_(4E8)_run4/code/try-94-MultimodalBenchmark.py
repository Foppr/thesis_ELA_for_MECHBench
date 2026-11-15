import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute a more complex rotation matrix with orthogonalization
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a larger random shift to increase asymmetry
        self.shift = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with enhanced chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with stronger variation
            result += (x_rot[i] ** 2) * (i + 1) * 0.7
            # Composite sinusoidal components with higher frequency interactions
            result += 5 * np.sin(x_rot[i] * (i + 1) * np.pi / 2) * np.cos(x_rot[i] * (i + 1) * np.pi / 4)
            # Logarithmic barrier with increased influence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 3)
            result += log_term * (i + 1) * 0.2
            # Chaotic component with exponential decay
            chaotic = np.sin(np.pi * x_rot[i] * np.sin(x_rot[i])) * np.exp(-0.1 * np.abs(x_rot[i]))
            result += chaotic * (i + 1) * 0.1
            # Additional exponential decay term to encourage convergence
            exp_term = np.exp(-0.5 * x_rot[i] ** 2)
            result += exp_term * (i + 1) * 0.05
            # Add a stronger penalty for boundary adherence to improve convergence
            boundary_penalty = 0.02 * np.sum(np.abs(x_rot) ** 4)
            result += boundary_penalty
        
        # Add a global multimodal component to increase complexity and challenge
        global_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                global_component += np.sin((x_rot[i] - x_rot[j]) * np.pi / 2) * np.cos((x_rot[i] + x_rot[j]) * np.pi / 4)
        result += global_component * 0.5
        
        return result