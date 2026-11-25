import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.lambda_params = np.random.uniform(0.5, 2.0, dim)
        self.delay_params = np.random.randint(1, 6, dim)
        self.feedback_strengths = np.random.uniform(0.1, 0.9, dim)
        self.attractor_centers = np.random.uniform(-3.0, 3.0, (dim, 3))
        self.phase_transitions = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system with time-delayed feedback
        chaotic_energy = 0.0
        for i in range(self.dim):
            # Delayed feedback term
            delayed_x = x[i] if self.delay_params[i] > len(x) else x[max(0, i - self.delay_params[i])]
            feedback = self.feedback_strengths[i] * (x[i] - delayed_x)
            
            # Logistic-like chaotic behavior
            lambda_param = self.lambda_params[i] * (1.0 + 0.2 * np.sin(0.3 * sum(x)))
            chaotic_energy += lambda_param * x[i] * (1.0 - x[i]**2) + feedback
            
        # Multi-attractor basin landscape
        attractor_term = 0.0
        for i in range(self.dim):
            distances = [np.linalg.norm(x[i] - center) for center in self.attractor_centers[i]]
            min_distance = min(distances)
            attractor_term += min_distance**2
            
        # Phase-transition induced ruggedness
        transition_term = 0.0
        for i in range(self.dim):
            phase_factor = self.phase_transitions[i] * np.sin(0.5 * x[i])
            transition_term += np.abs(np.tanh(phase_factor)) * (1.0 + 0.5 * np.cos(x[i]))
            
        # Non-smooth penalty terms with varying difficulty
        penalty_term = 0.0
        for i in range(self.dim):
            # Create non-differentiable points
            if abs(x[i]) < 0.1:
                penalty_term += 10.0 * np.abs(x[i])
            elif abs(x[i] - 2.0) < 0.5 or abs(x[i] + 2.0) < 0.5:
                penalty_term += 5.0 * (abs(x[i]) - 2.0)**2
                
        # Cross-dimensional coupling with varying strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling_strength = 0.5 * (1.0 + np.sin(0.2 * (x[i] + x[j])))
                coupling_term += coupling_strength * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Combine all terms with adaptive weights
        result = 0.4 * chaotic_energy + 0.3 * attractor_term + 0.2 * transition_term + \
                 0.1 * penalty_term + 0.5 * coupling_term
        
        return result