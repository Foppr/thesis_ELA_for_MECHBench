import numpy as np

class PolynomialRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos parameters
        self.poly_degrees = np.random.randint(3, 8, size=dim)
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, size=dim)
        # Ridge function parameters with adaptive scaling
        self.ridge_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.ridge_widths = np.random.uniform(0.3, 4.0, size=dim)
        self.ridge_amplitudes = np.random.uniform(2.0, 8.0, size=dim)
        # Dynamic gradient modulation parameters
        self.gradient_magnitude = np.random.uniform(0.3, 5.0, size=dim)
        self.gradient_frequency = np.random.uniform(0.05, 3.0, size=dim)
        self.gradient_phase = np.random.uniform(0, 4*np.pi, size=dim)
        # Connectivity and conditioning parameters
        self.conditioning_factors = np.random.uniform(0.05, 15.0, size=dim)
        self.connectivity_strength = np.random.uniform(0.2, 3.0, size=(dim, dim))
        # Fractal-based connectivity enhancement
        self.fractal_dimensions = np.random.uniform(1.1, 2.9, size=dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.5, size=dim)
        # Adaptive noise components
        self.noise_amplitude = np.random.uniform(0.05, 1.5, size=dim)
        self.noise_frequency = np.random.uniform(0.3, 4.0, size=dim)
        # Quantum-like probability distributions
        self.quantum_phases = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.1, 0.8, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component
        polynomial_term = 0.0
        for i in range(self.dim):
            poly_val = np.polyval([1] + [0]*(self.poly_degrees[i]-1) + [self.poly_coeffs[i]], x[i])
            polynomial_term += poly_val * self.conditioning_factors[i]
        
        # Ridge function component
        ridge_term = 0.0
        for i in range(self.dim):
            distance = np.abs(x[i] - self.ridge_centers[i])
            ridge_value = self.ridge_amplitudes[i] * np.exp(-distance**2 / (2 * self.ridge_widths[i]**2))
            ridge_term += ridge_value
        
        # Dynamic gradient modulation
        gradient_term = 0.0
        for i in range(self.dim):
            grad_val = self.gradient_magnitude[i] * np.sin(self.gradient_frequency[i] * x[i] + self.gradient_phase[i])
            gradient_term += grad_val * self.conditioning_factors[i]
        
        # Connectivity and conditioning effects with fractal enhancement
        connectivity_term = 0.0
        for i in range(self.dim):
            conn_val = 0.0
            for j in range(self.dim):
                if i != j:
                    conn_val += self.connectivity_strength[i, j] * np.sin(x[i] - x[j])
            # Fractal-based connectivity enhancement
            fractal_contribution = self.fractal_amplitudes[i] * np.sin(self.fractal_dimensions[i] * np.log(1 + np.abs(x[i])))
            connectivity_term += (conn_val + fractal_contribution) * self.conditioning_factors[i]
        
        # Adaptive noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_term += noise_val
        
        # Quantum-like probability distribution
        quantum_term = 0.0
        for i in range(self.dim):
            quantum_val = self.quantum_amplitudes[i] * np.cos(self.quantum_phases[i] * x[i])
            quantum_term += quantum_val
        
        # Combine all terms with different weights
        return (2.0 * polynomial_term + 
                2.5 * ridge_term + 
                1.5 * gradient_term + 
                1.0 * connectivity_term + 
                0.7 * noise_term + 
                0.3 * quantum_term)