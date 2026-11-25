import numpy as np

class QuaternionGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequencies and scaling factors
        self.frequencies = 2.0 + np.sin(np.arange(dim) * np.pi / (dim + 1))
        self.scaling = 1.0 + 0.5 * np.cos(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis functions with quaternion-inspired coupling
        f1 = 0.0
        for i in range(self.dim):
            # Quaternion-like interaction terms
            q_real = np.cos(x[i])
            q_imag = np.sin(x[i])
            f1 += self.scaling[i] * np.exp(-0.5 * (x[i]**2 + q_imag**2))
        
        # Cross-dimensional quaternion coupling with adaptive modulation
        f2 = 0.0
        for i in range(self.dim - 1):
            # Quaternion product-like interaction
            q_i_real = np.cos(x[i])
            q_i_imag = np.sin(x[i])
            q_ip1_real = np.cos(x[i+1])
            q_ip1_imag = np.sin(x[i+1])
            
            # Complex coupling with frequency modulation
            coupling = (q_i_real * q_ip1_real - q_i_imag * q_ip1_imag) * \
                       np.cos(self.frequencies[i] * x[i]) * \
                       np.sin(self.frequencies[i+1] * x[i+1])
            f2 += coupling
        
        # Adaptive polynomial with Gaussian modulation
        f3 = 0.3 * np.sum((x**4) * np.exp(-x**2 / 10.0))
        
        # Multi-scale harmonic components with dynamic phase shifts
        f4 = 0.25 * np.sum(np.sin(self.frequencies * x + np.cos(x)) * \
                          np.cos(2.0 * self.frequencies * x + np.sin(x)))
        
        # Sine-cosine coupled terms with adaptive weights
        f5 = 0.2 * np.sum(np.sin(x) * np.cos(3.0 * x) * np.exp(-np.abs(x) / 4.0))
        
        # Fractal-inspired recursive structure with Gaussian kernels
        f6 = 0.15 * np.sum(np.exp(-0.5 * (x - np.mean(x))**2) * \
                          np.sin(np.pi * x / 5.0) * \
                          np.cos(np.pi * x / 5.0))
        
        # Hyperbolic tangent with periodic modulation
        f7 = 0.12 * np.sum(np.tanh(x) * np.sin(2.0 * x) * np.exp(-x**2 / 8.0))
        
        # Cross-dimensional interaction with adaptive coupling strength
        cross_term = 0.0
        for i in range(self.dim - 1):
            # Adaptive coupling based on dimension and distance
            coupling_strength = 1.0 / (1.0 + np.abs(x[i] - x[i+1]))
            cross_term += coupling_strength * np.sin(x[i]) * np.cos(x[i+1])
        f8 = 0.1 * cross_term
        
        # Combined scaling factor based on dimension
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Return final function value with combined terms
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)