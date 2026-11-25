import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            freq = 2 + 3 * np.sin(i * np.pi / self.dim)
            amp = 1.5 + 0.5 * np.cos(i * np.pi / self.dim)
            sin_component += amp * np.sin(freq * xi) * np.cos(2 * xi)
        
        # Radial basis function with multiquadric kernels and varying shape parameters
        rbf_component = 0
        centers = np.linspace(-1, 1, min(6, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                shape_param = 0.3 + 0.7 * np.sin(i * np.pi / self.dim)
                rbf_component += np.sqrt((x_norm[i] - center)**2 + shape_param**2) * (1 + 0.2 * np.sin(5*i))
        
        # Asymmetric gradient field with polynomial and exponential components
        grad_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Asymmetric polynomial term
            poly_term = xi**3 + 0.5*xi**2 - 0.3*xi
            # Exponential bias towards negative values
            exp_bias = np.exp(-0.5 * xi**2) * (1 + 0.4 * np.sin(3*i))
            grad_component += poly_term * exp_bias * (1 + 0.3 * np.cos(7*i))
        
        # Cross-dimensional coupling with interaction strengths that vary by dimension
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength decreases with distance between dimensions - increased decay rate
                strength = 1.0 / (1.0 + abs(i - j) * 0.3)
                cross_coupling += strength * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(2*i*j)
        
        # Nonlinear transformation with chaotic logistic map behavior - altered chaotic parameters
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic map-like chaotic modulation with different control parameter
            logistic_map = 3.8 * xi * (1 - xi)
            chaotic_component += np.sin(10 * xi) * np.cos(8 * logistic_map) * (1 + 0.2 * np.sin(3*i))
        
        # Add periodic boundary effect with multiple harmonics
        periodic_effect = 0
        for i in range(self.dim):
            xi = x_norm[i]
            periodic_effect += (np.sin(2*np.pi*xi) + 0.5*np.sin(4*np.pi*xi) + 
                              0.3*np.sin(6*np.pi*xi)) * np.cos(2*i)
        
        # Combine all components with adaptive weights - adjusted coefficients
        result = 1.0 * sin_component + 1.2 * rbf_component + 1.8 * grad_component + \
                1.0 * cross_coupling + 1.5 * chaotic_component + 0.7 * periodic_effect
        
        # Add controlled noise for robustness
        noise = np.random.normal(0, 0.003)
        
        return result + noise