import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.chaotic_params = np.random.uniform(0.1, 2.0, dim)
        self.delay_params = np.random.uniform(0.5, 2.0, dim)
        self.bifurcation_points = np.random.uniform(2.5, 4.0, dim)
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        self.coupling_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        self.feedback_delays = np.random.randint(1, 6, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic dynamical system with time-delayed feedback
        result = 0.0
        for i in range(self.dim):
            # Logistic map with bifurcation parameter
            chaotic_value = x_norm[i]
            for _ in range(10):  # Iterate to reach chaotic regime
                chaotic_value = self.bifurcation_points[i] * chaotic_value * (1 - chaotic_value)
            
            # Time-delayed feedback component
            delay_effect = 0.0
            for j in range(self.feedback_delays[i]):
                if i-j >= 0:
                    delay_effect += self.delay_params[i] * x_norm[i-j] * np.sin(j * np.pi / 4)
            
            # Modified Chebyshev polynomial terms
            chebyshev_value = 0.0
            for k in range(5):
                T_k = np.cos(k * np.arccos(np.clip(x_norm[i], -1, 1)))
                chebyshev_value += self.chebyshev_coeffs[i, k] * T_k
            
            # Combine chaotic and polynomial components
            result += self.chaotic_params[i] * (chaotic_value + delay_effect + chebyshev_value)
        
        # Cross-dimensional coupling terms with nonlinear interactions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = self.coupling_strengths[i, j]
                # Nonlinear coupling with sine and cosine functions
                coupling = coupling_strength * np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                coupling_terms += coupling
        
        # Add saddle-node bifurcation effects
        bifurcation_effects = 0.0
        for i in range(self.dim):
            # Saddle-node bifurcation term with threshold
            threshold = 0.5 * (1 + np.tanh(x_norm[i]))
            bifurcation_effects += threshold * np.exp(-x_norm[i]**2)
        
        # Combine all components with additional nonlinearity
        total = result + 0.3 * coupling_terms + 0.2 * bifurcation_effects
        
        # Apply nonlinear transformation for increased complexity
        total = np.tanh(total) * (1.0 + 0.15 * np.sin(np.sum(x_norm**3)))
        
        # Add small noise for robustness
        noise = np.random.normal(0, 0.005)
        total += noise
        
        return total