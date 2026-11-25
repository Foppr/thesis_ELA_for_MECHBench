import numpy as np

class ChaoticSpectralSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced sinusoidal oscillation with spectral decomposition and varying frequencies
        sin_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            freq = 3 + 4 * np.sin(i * np.pi / self.dim)
            amp = 2.0 + 0.8 * np.cos(i * np.pi / self.dim)
            sin_component += amp * np.sin(freq * xi) * np.cos(3 * xi) * np.exp(-0.1 * i)
        
        # Radial basis function with multiquadric kernels and variable shape parameters
        rbf_component = 0
        centers = np.linspace(-1, 1, min(8, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                shape_param = 0.2 + 0.6 * np.sin(i * np.pi / self.dim)
                rbf_component += np.sqrt((x_norm[i] - center)**2 + shape_param**2) * (1 + 0.3 * np.sin(7*i))
        
        # Asymmetric gradient field with polynomial, exponential, and hyperbolic components
        grad_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Asymmetric polynomial term with higher degree
            poly_term = xi**5 + 0.7*xi**3 - 0.4*xi**2 + 0.1*xi
            # Exponential bias towards negative values with hyperbolic tangent modulation
            exp_bias = np.tanh(0.5 * xi) * (1 + 0.5 * np.sin(4*i))
            grad_component += poly_term * exp_bias * (1 + 0.4 * np.cos(9*i))
        
        # Cross-dimensional coupling with enhanced interaction strengths and non-linear decay
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength with faster decay rate and sinusoidal modulation
                strength = 1.5 / (1.0 + abs(i - j)**1.8 * 0.4) * (1 + 0.3 * np.sin(2*i + 3*j))
                cross_coupling += strength * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(3*i*j)
        
        # Chaotic tent map component with enhanced nonlinearity and multiple attractors
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map-like chaotic modulation with multiple control parameters
            if xi < 0.5:
                tent_map = 2 * xi
            else:
                tent_map = 2 * (1 - xi)
            chaotic_component += np.sin(12 * xi) * np.cos(10 * tent_map) * (1 + 0.3 * np.sin(4*i))
        
        # Saddle-point interaction with varying curvature and multiple local minima
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Saddle point with hyperbolic sine and cosine components
            saddle_component += (np.sinh(xi) * np.cos(5*xi) + np.cosh(xi) * np.sin(3*xi)) * (1 + 0.2 * np.sin(6*i))
        
        # Add periodic boundary effect with multiple harmonics and phase shifts
        periodic_effect = 0
        for i in range(self.dim):
            xi = x_norm[i]
            periodic_effect += (np.sin(3*np.pi*xi) + 0.6*np.sin(6*np.pi*xi) + 
                              0.4*np.sin(9*np.pi*xi) + 0.2*np.sin(12*np.pi*xi)) * np.cos(3*i)
        
        # Combine all components with adaptive weights - increased complexity and nonlinearity
        result = 1.5 * sin_component + 1.8 * rbf_component + 2.2 * grad_component + \
                1.8 * cross_coupling + 2.0 * chaotic_component + 1.2 * saddle_component + \
                0.9 * periodic_effect
        
        # Add controlled noise for robustness and increased difficulty
        noise = np.random.normal(0, 0.005)
        
        return result + noise