import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher variability
        self.lambda_params = np.random.uniform(0.1, 3.0, dim)
        self.delay_params = np.random.randint(1, 10, dim)
        self.feedback_strengths = np.random.uniform(0.05, 1.2, dim)
        self.attractor_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.phase_transitions = np.random.uniform(0.2, 3.0, dim)
        # Additional parameters for increased complexity
        self.nonlinear_weights = np.random.uniform(0.5, 2.0, dim)
        self.coupling_strengths = np.random.uniform(0.3, 1.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system with time-delayed feedback and higher nonlinearity
        chaotic_energy = 0.0
        for i in range(self.dim):
            # Delayed feedback term with more complex dependency
            delayed_x = x[i] if self.delay_params[i] > len(x) else x[max(0, i - self.delay_params[i])]
            feedback = self.feedback_strengths[i] * (x[i] - delayed_x) * np.exp(-0.1 * abs(x[i]))
            
            # Enhanced chaotic behavior with variable lambda
            lambda_param = self.lambda_params[i] * (1.0 + 0.3 * np.sin(0.5 * sum(x)) + 0.2 * np.cos(0.7 * sum(x)))
            chaotic_energy += lambda_param * x[i] * (1.0 - x[i]**2) * (1.0 + 0.1 * np.sin(2.0 * x[i])) + feedback
            
        # Multi-attractor basin landscape with more attractors
        attractor_term = 0.0
        for i in range(self.dim):
            distances = [np.linalg.norm(x[i] - center) for center in self.attractor_centers[i]]
            min_distance = min(distances)
            attractor_term += min_distance**3 + 0.5 * np.sin(0.5 * min_distance)
            
        # Phase-transition induced ruggedness with enhanced complexity
        transition_term = 0.0
        for i in range(self.dim):
            phase_factor = self.phase_transitions[i] * np.sin(1.0 * x[i]) + 0.3 * np.cos(1.5 * x[i])
            transition_term += np.abs(np.tanh(phase_factor)) * (1.0 + 0.4 * np.cos(0.8 * x[i])) + \
                              0.2 * np.sin(2.0 * x[i]) * np.exp(-0.05 * abs(x[i]))
            
        # Non-smooth penalty terms with increased complexity
        penalty_term = 0.0
        for i in range(self.dim):
            # Create multiple non-differentiable points and sharp changes
            if abs(x[i]) < 0.05:
                penalty_term += 20.0 * np.abs(x[i])
            elif abs(x[i] - 1.5) < 0.3 or abs(x[i] + 1.5) < 0.3:
                penalty_term += 10.0 * (abs(x[i]) - 1.5)**2
            elif abs(x[i] - 3.0) < 0.4 or abs(x[i] + 3.0) < 0.4:
                penalty_term += 15.0 * np.log(1.0 + abs(x[i]))
                
        # Enhanced cross-dimensional coupling with full connectivity
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.coupling_strengths[i, j] * (1.0 + 0.3 * np.sin(0.4 * (x[i] + x[j])))
                    coupling_term += coupling_strength * np.exp(-0.2 * (x[i] - x[j])**2) * \
                                    (1.0 + 0.1 * np.cos(0.6 * (x[i] + x[j])))
                
        # Combine all terms with adaptive weights
        result = 0.35 * chaotic_energy + 0.25 * attractor_term + 0.18 * transition_term + \
                 0.17 * penalty_term + 0.05 * coupling_term
        
        return result