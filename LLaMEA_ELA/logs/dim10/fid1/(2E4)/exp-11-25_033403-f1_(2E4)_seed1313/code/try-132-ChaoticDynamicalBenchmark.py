import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.lambda_params = np.random.uniform(0.1, 0.9, dim)
        self.delay_params = np.random.randint(1, 5, dim)
        self.bifurcation_params = np.random.uniform(2.5, 4.0, dim)
        self.mixing_weights = np.random.dirichlet(np.ones(dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system component with time-delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            # Time-delayed logistic map with chaotic dynamics
            delay = self.delay_params[i]
            if i >= delay:
                x_delayed = x[i - delay]
            else:
                x_delayed = x[i]  # Boundary condition
            
            # Saddle-node bifurcation mechanism
            bifurcation_factor = self.bifurcation_params[i]
            chaotic_term += (self.lambda_params[i] * x[i] * (1.0 - x[i]) * 
                           np.sin(bifurcation_factor * x[i]) * 
                           np.exp(-0.1 * np.abs(x[i] - x_delayed)))
        
        # Ergodic mixing component with multi-scale interaction
        mixing_term = 0.0
        for i in range(self.dim):
            # Multi-scale mixing using different frequency components
            freq_components = [1.0, 2.0, 3.0, 4.0]
            mixing_sum = 0.0
            for freq in freq_components:
                mixing_sum += np.sin(freq * x[i]) * np.cos(freq * x[i])
            mixing_term += self.mixing_weights[i] * mixing_sum
        
        # Cross-dimensional coupling with feedback loops
        feedback_term = 0.0
        for i in range(self.dim):
            # Create feedback connections between dimensions
            feedback_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Nonlinear feedback with distance-based weighting
                    dist = np.abs(x[i] - x[j])
                    weight = 1.0 / (1.0 + dist)
                    feedback_sum += weight * np.tanh(x[j] * np.sin(0.5 * x[i]))
            feedback_term += feedback_sum
        
        # Multi-modal structure with chaotic basin boundaries
        modal_term = 0.0
        for i in range(self.dim):
            # Create complex landscape using chaotic attractor-like structures
            modal_term += (np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * 
                          np.exp(-0.05 * x[i]**2) + 
                          0.1 * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]))
        
        # Add dynamic penalty for boundary avoidance
        boundary_penalty = 0.0
        for i in range(self.dim):
            penalty = 10.0 * (np.exp(-0.5 * (x[i] - 5.0)**2) + 
                            np.exp(-0.5 * (x[i] + 5.0)**2))
            boundary_penalty += penalty
        
        # Combine all components with adaptive weights
        total = 0.6 * chaotic_term + 0.7 * mixing_term + 0.5 * feedback_term + 0.8 * modal_term + 0.4 * boundary_penalty
        
        return total