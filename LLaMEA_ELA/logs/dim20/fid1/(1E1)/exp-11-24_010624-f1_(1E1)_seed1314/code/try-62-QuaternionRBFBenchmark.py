import numpy as np

class QuaternionRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quaternion-like parameters for cross-dimensional interactions
        self.quat_params = np.array([np.cos(i * 0.5) + 1j * np.sin(i * 0.5) for i in range(dim)])
        # Radial basis function centers and widths
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Radial basis function component
        for i in range(10):
            diff = x - self.centers[i]
            rbf_value = self.widths[i] * np.exp(-0.5 * np.sum(diff**2))
            result += rbf_value
            
        # Quaternion-inspired cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use quaternion-like interaction with imaginary components
                q_i = self.quat_params[i]
                q_j = self.quat_params[j]
                interaction = np.real(q_i * np.conj(q_j) * (x[i] * x[j]))
                result += 0.1 * interaction * np.sin(0.3 * (x[i]**2 + x[j]**2))
                
        # Adaptive noise component based on position
        noise_amp = 0.05 * (1 + 0.5 * np.sin(np.sum(x**2) * 0.1))
        noise = noise_amp * np.random.normal(0, 1)
        result += noise
        
        # Add polynomial modulation with frequency variation
        poly_mod = 0.02 * np.sum((x**3) * np.cos(0.5 * x))
        result += poly_mod
        
        # Global scaling with dynamic factor
        dist = np.sqrt(np.sum(x**2))
        scale_factor = 1 + 0.2 * np.sin(0.4 * dist) * np.cos(0.6 * dist)
        result *= scale_factor
        
        return result