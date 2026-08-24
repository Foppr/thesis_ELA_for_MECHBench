import numpy as np

class ChaoticRotationalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotational symmetry parameters
        np.random.seed(42)
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim)
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.basis_centers = np.random.uniform(-3.0, 3.0, (dim, 3))
        self.amplitude_factors = np.random.uniform(0.5, 2.5, dim)
        self.periodic_freqs = np.random.uniform(1.0, 5.0, dim)
        self.quaternion_weights = np.random.uniform(-1.0, 1.0, (dim, 4))
        self.scale_factor = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply exponential decay scaling
        decay_scaled = x * np.exp(-self.decay_rates * np.abs(x))
        
        # Radial basis function component
        rb_func = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = self.basis_centers[i, j]
                rb_func += np.exp(-0.5 * ((x[i] - center) / (0.5 + j))**2)
        
        # Quaternion-inspired rotational symmetry
        quat_sum = 0.0
        for i in range(self.dim):
            q = self.quaternion_weights[i]
            rot_term = q[0]*np.sin(self.rotation_angles[i] + x[i]) + \
                       q[1]*np.cos(self.rotation_angles[i] + x[i]) + \
                       q[2]*np.sin(2*self.rotation_angles[i] + x[i]) + \
                       q[3]*np.cos(2*self.rotation_angles[i] + x[i])
            quat_sum += rot_term
        
        # Periodic oscillation with amplitude modulation
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += self.amplitude_factors[i] * \
                            np.sin(self.periodic_freqs[i] * x[i]) * \
                            np.cos(self.periodic_freqs[i] * x[i] / 2.0)
        
        # Combined chaotic landscape
        f_val = np.sum(decay_scaled**2) + \
                0.3 * rb_func + \
                0.5 * quat_sum**2 + \
                0.2 * periodic_term**2 + \
                0.1 * np.sum(np.abs(x)) + \
                0.05 * np.sum(np.sin(x)**2)
        
        # Add multi-scale structure through nested sinusoids
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.1 * x[i]**2)
        f_val += 0.15 * nested_term
        
        return f_val