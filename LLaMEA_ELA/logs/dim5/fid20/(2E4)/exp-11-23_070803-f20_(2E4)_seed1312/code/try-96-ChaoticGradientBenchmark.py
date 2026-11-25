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
            freq = 3 + 4 * np.sin(i * np.pi / self.dim)
            amp = 2.0 + 0.8 * np.cos(i * np.pi / self.dim)
            sin_component += amp * np.sin(freq * xi) * np.cos(3 * xi)
        
        # Radial basis function with multiquadric kernels and varying shape parameters
        rbf_component = 0
        centers = np.linspace(-1, 1, min(8, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                shape_param = 0.2 + 0.6 * np.sin(i * np.pi / self.dim)
                rbf_component += np.sqrt((x_norm[i] - center)**2 + shape_param**2) * (1 + 0.3 * np.sin(7*i))
        
        # Asymmetric gradient field with polynomial and exponential components
        grad_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Asymmetric polynomial term with higher order terms
            poly_term = xi**5 + 0.7*xi**3 - 0.4*xi**2 + 0.2*xi
            # Exponential bias towards negative values with periodic modulation
            exp_bias = np.exp(-0.3 * xi**2) * (1 + 0.5 * np.sin(5*i)) * (1 + 0.2 * np.cos(4*i))
            grad_component += poly_term * exp_bias * (1 + 0.4 * np.cos(9*i))
        
        # Cross-dimensional coupling with interaction strengths that vary by dimension
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength decreases with distance between dimensions
                strength = 1.0 / (1.0 + abs(i - j) * 0.15)
                cross_coupling += strength * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(3*i*j)
        
        # Nonlinear transformation with chaotic logistic map behavior and quaternion-like symmetry
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic map-like chaotic modulation with higher sensitivity
            logistic_map = 4 * xi * (1 - xi)
            chaotic_component += np.sin(12 * xi) * np.cos(9 * logistic_map) * (1 + 0.3 * np.sin(5*i))
        
        # Saddle-point enhancement with rotational symmetry components
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Add saddle-like behavior with multiple quadratic terms
            saddle_component += (xi**2 - 1)**2 * np.sin(5*xi) * (1 + 0.25 * np.cos(6*i))
        
        # Add periodic boundary effect with multiple harmonics and phase shifts
        periodic_effect = 0
        for i in range(self.dim):
            xi = x_norm[i]
            periodic_effect += (np.sin(3*np.pi*xi) + 0.6*np.sin(6*np.pi*xi) + 
                              0.4*np.sin(9*np.pi*xi)) * np.cos(3*i)
        
        # Combine all components with adaptive weights
        result = 1.5 * sin_component + 1.2 * rbf_component + 1.8 * grad_component + \
                1.0 * cross_coupling + 1.6 * chaotic_component + 0.8 * saddle_component + \
                0.7 * periodic_effect
        
        # Add controlled noise for robustness
        noise = np.random.normal(0, 0.005)
        
        return result + noise