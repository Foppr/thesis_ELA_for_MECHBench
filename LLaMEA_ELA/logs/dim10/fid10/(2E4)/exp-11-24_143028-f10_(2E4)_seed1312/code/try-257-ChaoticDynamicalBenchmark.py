import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher variability
        self.lambda_params = np.random.uniform(0.1, 4.0, dim)
        self.delay_params = np.random.randint(1, 15, dim)
        self.feedback_strengths = np.random.uniform(0.02, 1.5, dim)
        self.attractor_centers = np.random.uniform(-4.0, 4.0, (dim, 7))
        self.phase_transitions = np.random.uniform(0.1, 4.0, dim)
        # Additional parameters for increased complexity
        self.nonlinear_weights = np.random.uniform(0.3, 2.5, dim)
        self.coupling_strengths = np.random.uniform(0.2, 2.0, (dim, dim))
        # Quantum-inspired interference terms
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        self.interference_strengths = np.random.uniform(0.5, 3.0, dim)
        # Topological constraints
        self.topo_curvatures = np.random.uniform(-0.5, 0.5, dim)
        self.hole_radii = np.random.uniform(0.1, 2.0, dim)
        
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
            lambda_param = self.lambda_params[i] * (1.0 + 0.4 * np.sin(0.5 * sum(x)) + 0.3 * np.cos(0.7 * sum(x)) + 0.2 * np.sin(1.3 * sum(x)))
            chaotic_energy += lambda_param * x[i] * (1.0 - x[i]**2) * (1.0 + 0.15 * np.sin(2.0 * x[i]) + 0.1 * np.cos(3.0 * x[i])) + feedback
            
        # Multi-attractor basin landscape with more attractors
        attractor_term = 0.0
        for i in range(self.dim):
            distances = [np.linalg.norm(x[i] - center) for center in self.attractor_centers[i]]
            min_distance = min(distances)
            attractor_term += min_distance**3 + 0.5 * np.sin(0.5 * min_distance) + 0.2 * np.cos(1.5 * min_distance)
            
        # Phase-transition induced ruggedness with enhanced complexity
        transition_term = 0.0
        for i in range(self.dim):
            phase_factor = self.phase_transitions[i] * np.sin(0.7 * x[i]) + 0.3 * np.cos(1.2 * x[i]) + 0.1 * np.sin(2.0 * x[i])
            transition_term += np.abs(np.tanh(phase_factor)) * (1.0 + 0.4 * np.cos(0.8 * x[i])) + \
                              0.2 * np.sin(1.5 * x[i]) * np.exp(-0.05 * abs(x[i])) + \
                              0.15 * np.cos(2.5 * x[i])
            
        # Non-smooth penalty terms with increased complexity
        penalty_term = 0.0
        for i in range(self.dim):
            # Create multiple non-differentiable points and sharp changes
            if abs(x[i]) < 0.03:
                penalty_term += 20.0 * np.abs(x[i])
            elif abs(x[i] - 1.5) < 0.2 or abs(x[i] + 1.5) < 0.2:
                penalty_term += 10.0 * (abs(x[i]) - 1.5)**2
            elif abs(x[i] - 3.0) < 0.3 or abs(x[i] + 3.0) < 0.3:
                penalty_term += 15.0 * np.log(1.0 + abs(x[i]))
            elif abs(x[i] - 4.0) < 0.2 or abs(x[i] + 4.0) < 0.2:
                penalty_term += 25.0 * (abs(x[i]) - 4.0)**3
                
        # Quantum-inspired interference terms
        quantum_term = 0.0
        for i in range(self.dim):
            quantum_phase = self.quantum_phases[i] + 0.3 * np.sin(0.8 * x[i])
            interference = self.interference_strengths[i] * np.sin(quantum_phase) * np.cos(1.5 * x[i])
            quantum_term += interference
            
        # Topological constraints with curvature and hole effects
        topo_term = 0.0
        for i in range(self.dim):
            # Curvature effect
            curvature_effect = self.topo_curvatures[i] * x[i]**2
            # Hole effect - penalty when close to specific values
            hole_penalty = 0.0
            for r in self.hole_radii:
                if abs(x[i] - r) < 0.1 or abs(x[i] + r) < 0.1:
                    hole_penalty += 50.0 * (abs(x[i]) - r)**2
            
            topo_term += curvature_effect + hole_penalty
            
        # Enhanced cross-dimensional coupling with full connectivity
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.coupling_strengths[i, j] * (1.0 + 0.3 * np.sin(0.4 * (x[i] + x[j])) + 0.2 * np.cos(0.6 * (x[i] - x[j])))
                    coupling_term += coupling_strength * np.exp(-0.2 * (x[i] - x[j])**2) * \
                                    (1.0 + 0.1 * np.cos(0.6 * (x[i] + x[j])) + 0.05 * np.sin(1.2 * (x[i] - x[j])))
                
        # Combine all terms with adaptive weights
        result = 0.25 * chaotic_energy + 0.2 * attractor_term + 0.18 * transition_term + \
                 0.12 * penalty_term + 0.08 * quantum_term + 0.07 * topo_term + 0.1 * coupling_term
        
        return result