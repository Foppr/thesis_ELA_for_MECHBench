import numpy as np

class ExponentialRotationalPenaltyLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.decay_amplitudes = np.random.uniform(1.0, 5.0, dim)
        # Initialize quaternion-based rotational components
        self.quat_weights = np.random.uniform(0.5, 2.0, (4, dim))
        self.quat_angles = np.random.uniform(0, 2*np.pi, (4, dim))
        # Initialize penalty parameters with shifted centers
        self.penalty_centers = np.random.uniform(-2.5, 2.5, dim)
        self.penalty_strengths = np.random.uniform(1.0, 4.0, dim)
        self.penalty_widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute exponential decay components
        exp_terms = 0.0
        for j in range(self.dim):
            exp_term = self.decay_amplitudes[j] * np.exp(-self.decay_rates[j] * np.abs(x[j]))
            exp_terms += exp_term
        
        # Compute quaternion-based rotational components with interaction terms
        rot_terms = 0.0
        for i in range(4):
            quat_rot = 0.0
            for j in range(self.dim):
                quat_rot += self.quat_weights[i, j] * np.sin(self.quat_angles[i, j] * x[j])
            rot_terms += quat_rot**2
        
        # Compute penalty components with additional nonlinear interaction
        penalty_terms = 0.0
        for j in range(self.dim):
            distance = np.abs(x[j] - self.penalty_centers[j])
            penalty = self.penalty_strengths[j] * np.exp(-0.5 * (distance / self.penalty_widths[j])**2)
            # Add nonlinear interaction term
            penalty += 0.1 * np.sin(3.0 * distance) * np.cos(2.0 * x[j])
            penalty_terms += penalty
        
        # Combine all components with modified weights
        total = 0.6 * exp_terms + 0.4 * rot_terms + 0.5 * penalty_terms
        
        return total