import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Add a chaotic parameter that influences the landscape
        self.chaotic_param = np.random.uniform(0.5, 2.0)
        # Add a new hyperparameter for increased complexity
        self.hyper_param = np.random.uniform(0.1, 1.0)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Sinusoidal components with varying frequencies and amplitudes
            result += 5 * np.sin(x_rot[i] * (i + 1) * np.pi / 2) * np.cos(x_rot[i] * (i + 1) * np.pi / 4)
            # Logarithmic barrier to prevent divergence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 2)
            result += log_term * (i + 1) * 0.15
            # Additional chaotic component using a tent map-like term
            chaotic = np.sin(np.pi * x_rot[i] * np.sin(x_rot[i] * self.chaotic_param))
            result += chaotic * (i + 1) * 0.1
            # Exponential decay term to create ruggedness
            exp_term = np.exp(-0.1 * np.abs(x_rot[i]))
            result += exp_term * (i + 1) * 0.05
            # Add a composite sinusoidal term for increased multimodality
            composite = np.sin(x_rot[i] * np.pi * (i + 1)) * np.cos(x_rot[i] * np.pi * (i + 1) / 2)
            result += composite * (i + 1) * 0.08
            # Add a new hyperbolic tangent component for additional complexity
            tanh_component = np.tanh(x_rot[i] * self.hyper_param) * (i + 1) * 0.2
            result += tanh_component
            # Add a fifth-order polynomial term to increase landscape ruggedness
            poly_term = (x_rot[i] ** 5) * 0.001 * (i + 1)
            result += poly_term
            # Add a new sinusoidal term with a different frequency pattern
            new_sin = np.sin(x_rot[i] * np.pi * (i + 1) * 1.5) * 0.1 * (i + 1)
            result += new_sin
        
        # Add a penalty for large values to encourage convergence
        result += 0.002 * np.sum(np.abs(x_rot) ** 4)
        
        # Add a new penalty term based on the product of all dimensions
        product_penalty = np.prod(np.abs(x_rot)) * 0.0005
        result += product_penalty
        
        return result