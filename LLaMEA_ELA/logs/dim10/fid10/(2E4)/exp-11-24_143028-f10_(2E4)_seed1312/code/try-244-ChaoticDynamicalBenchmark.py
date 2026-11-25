import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher variability
        self.lambda_params = np.random.uniform(0.8, 3.0, dim)
        self.delay_params = np.random.randint(2, 10, dim)
        self.feedback_strengths = np.random.uniform(0.2, 1.0, dim)
        self.attractor_centers = np.random.uniform(-4.0, 4.0, (dim, 4))
        self.phase_transitions = np.random.uniform(0.3, 2.5, dim)
        # Additional chaotic parameters for complexity
        self.chaos_mixing = np.random.uniform(0.1, 0.9, dim)
        self.nonlinear_exponents = np.random.uniform(1.5, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic dynamical system with time-delayed feedback
        chaotic_energy = 0.0
        for i in range(self.dim):
            # Extended delayed feedback term with mixing
            delayed_x = x[i] if self.delay_params[i] > len(x) else x[max(0, i - self.delay_params[i])]
            feedback = self.feedback_strengths[i] * (x[i] - delayed_x)
            
            # Enhanced logistic-like chaotic behavior with nonlinear exponents
            lambda_param = self.lambda_params[i] * (1.0 + 0.3 * np.sin(0.4 * sum(x)))
            nonlinear_term = x[i]**self.nonlinear_exponents[i]
            chaotic_energy += lambda_param * nonlinear_term * (1.0 - x[i]**2) + feedback
            
        # Multi-attractor basin landscape with more attractors
        attractor_term = 0.0
        for i in range(self.dim):
            distances = [np.linalg.norm(x[i] - center) for center in self.attractor_centers[i]]
            min_distance = min(distances)
            attractor_term += min_distance**2
            
        # Enhanced phase-transition induced ruggedness with multiple transition points
        transition_term = 0.0
        for i in range(self.dim):
            phase_factor1 = self.phase_transitions[i] * np.sin(0.6 * x[i])
            phase_factor2 = self.phase_transitions[i] * np.cos(0.4 * x[i])
            transition_term += (np.abs(np.tanh(phase_factor1)) + 0.5 * np.abs(np.tanh(phase_factor2))) * \
                              (1.0 + 0.3 * np.cos(x[i]) + 0.2 * np.sin(2*x[i]))
            
        # Enhanced non-smooth penalty terms with more complex structure
        penalty_term = 0.0
        for i in range(self.dim):
            # Create multiple non-differentiable points
            if abs(x[i]) < 0.05:
                penalty_term += 15.0 * np.abs(x[i])
            elif abs(x[i] - 1.5) < 0.3 or abs(x[i] + 1.5) < 0.3:
                penalty_term += 8.0 * (abs(x[i]) - 1.5)**2
            elif abs(x[i] - 3.0) < 0.4 or abs(x[i] + 3.0) < 0.4:
                penalty_term += 6.0 * np.log(1.0 + abs(x[i] - 3.0))
                
        # Enhanced cross-dimensional coupling with stronger interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                coupling_strength = 0.7 * (1.0 + np.sin(0.3 * (x[i] + x[j])) + 
                                          0.3 * np.cos(0.2 * (x[i] - x[j])))
                coupling_term += coupling_strength * np.exp(-0.15 * (x[i] - x[j])**2) * \
                                (1.0 + 0.1 * np.sin(0.5 * sum(x)))
                
        # Combine all terms with adaptive weights
        result = 0.3 * chaotic_energy + 0.25 * attractor_term + 0.2 * transition_term + \
                 0.15 * penalty_term + 0.1 * coupling_term
        
        return result