import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.feedback_coefficients = np.random.uniform(0.1, 0.9, dim)
        self.delay_parameters = np.random.randint(1, 5, dim)
        self.attractor_strengths = np.random.uniform(1.0, 5.0, dim)
        self.phase_transitions = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system component
        chaotic_term = 0.0
        for i in range(self.dim):
            # Time-delayed feedback with chaotic dynamics
            feedback = self.feedback_coefficients[i] * np.sin(x[i] + np.sum(x) / self.dim)
            delayed_x = x[(i - self.delay_parameters[i]) % self.dim]
            chaotic_term += self.attractor_strengths[i] * (x[i]**2 - delayed_x**2) * np.exp(-0.1 * feedback**2)
            
        # Multi-attractor basins
        attractor_term = 0.0
        for i in range(self.dim):
            # Multiple local minima based on phase transitions
            phase = self.phase_transitions[i] * x[i]
            attractor_term += np.sin(phase) * np.cos(phase) * np.exp(-0.05 * x[i]**2)
            
        # Phase-transition induced ruggedness
        ruggedness_term = 0.0
        for i in range(self.dim):
            # Create non-smooth regions using absolute values and step functions
            ruggedness_term += np.abs(x[i]) * np.sin(10 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Cross-dimensional coupling with chaotic interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling between dimensions
                coupling = np.sin(x[i] - x[j]) * np.exp(-0.01 * (x[i] - x[j])**2)
                coupling_term += coupling * (self.attractor_strengths[i] + self.attractor_strengths[j])
                
        # Adaptive conditioning based on dimensionality
        adaptive_factor = np.log(self.dim + 1) + 1.0
        
        # Combine all components with dynamic weights
        result = adaptive_factor * chaotic_term + 0.3 * attractor_term + 0.4 * ruggedness_term + 0.2 * coupling_term
        
        return result