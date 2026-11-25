import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=(dim, 5))
        # Adaptive neural-like weights with dynamic scaling
        self.neural_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        self.neural_bias = np.random.uniform(-0.5, 0.5, size=dim)
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        # Fractal Brownian motion parameters
        self.hurst_exponent = np.random.uniform(0.1, 0.9, size=dim)
        self.fractal_amplitude = np.random.uniform(0.5, 3.0, size=dim)
        # Adaptive coupling strengths with time-varying parameters
        self.coupling_strengths = np.random.uniform(0.1, 2.0, size=dim)
        self.adaptive_factors = np.random.uniform(0.8, 1.5, size=dim)
        # Chaotic logistic map parameters for dynamic behavior
        self.logistic_r = np.random.uniform(3.5, 4.0, size=dim)
        # Multi-scale harmonic components with varying frequencies
        self.harmonic_freqs = np.random.uniform(1.0, 8.0, size=dim)
        self.harmonic_amplitudes = np.random.uniform(0.5, 2.5, size=dim)
        # Nonlinear activation functions with parameterized shapes
        self.activation_params = np.random.uniform(0.5, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            x_scaled = x[i] / 5.0
            poly_term = (self.poly_coeffs[i, 0] + 
                        self.poly_coeffs[i, 1] * x_scaled + 
                        self.poly_coeffs[i, 2] * x_scaled**2 + 
                        self.poly_coeffs[i, 3] * x_scaled**3 + 
                        self.poly_coeffs[i, 4] * x_scaled**4)
            poly_component += poly_term * self.scaling_factors[i]
        
        # Neural network-like adaptive interaction
        neural_component = 0.0
        for i in range(self.dim):
            activation_input = np.sum(self.neural_weights[i, :] * x) + self.neural_bias[i]
            # Adaptive activation function with parameterized shape
            neural_output = np.tanh(activation_input * self.activation_params[i])
            neural_component += neural_output * self.coupling_strengths[i]
        
        # Fractal Brownian motion based ruggedness
        fbm_component = 0.0
        for i in range(self.dim):
            # Simple fractal-like component using power law scaling
            fractal_term = np.sin(x[i] * self.harmonic_freqs[i]) * self.fractal_amplitude[i]
            fbm_component += fractal_term * (1.0 + 0.3 * np.sin(2 * x[i]))
        
        # Chaotic logistic map dynamics
        logistic_component = 0.0
        for i in range(self.dim):
            # Use previous dimension's value for chaotic coupling
            prev_val = x[(i-1) % self.dim] if i > 0 else x[-1]
            logistic_val = self.logistic_r[i] * prev_val * (1 - prev_val)
            logistic_component += logistic_val * self.coupling_strengths[i]
        
        # Multi-scale harmonic interference
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_term = (np.sin(x[i] * self.harmonic_freqs[i]) * 
                           np.cos(x[i] * self.harmonic_freqs[i] * 0.5) * 
                           self.harmonic_amplitudes[i])
            harmonic_component += harmonic_term
        
        # Adaptive coupling with dynamic factors
        adaptive_component = 0.0
        for i in range(self.dim):
            coupling_val = x[i] * (1 + 0.2 * np.sin(x[(i+1) % self.dim]))
            adaptive_component += coupling_val * self.adaptive_factors[i]
        
        # Combined fitness function with weighted components
        return (1.5 * poly_component + 
                1.2 * neural_component + 
                0.8 * fbm_component + 
                1.0 * logistic_component + 
                0.9 * harmonic_component + 
                0.7 * adaptive_component)