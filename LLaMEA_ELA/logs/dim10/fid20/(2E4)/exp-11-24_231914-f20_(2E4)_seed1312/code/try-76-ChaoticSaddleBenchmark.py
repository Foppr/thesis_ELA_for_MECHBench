import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodicity and chaos parameters
        self.periods = [2.0, 3.0, 5.0, 7.0, 11.0][:min(dim, 5)]
        self.chaos_params = [0.5, 0.7, 0.9, 0.6, 0.8][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Chaotic saddle component with discontinuous gradients
        chaotic_saddle = 0.0
        for i in range(self.dim):
            # Saddle-like behavior with exponential decay
            chaotic_saddle += (np.sin(self.periods[i % len(self.periods)] * x[i]) * 
                              np.cos(self.chaos_params[i % len(self.chaos_params)] * x[i]**2) *
                              np.exp(-0.1 * np.abs(x[i])) + 
                              0.3 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * 
                              np.exp(-0.2 * x[i]**2))
        
        # Embedded periodic attractor landscape
        periodic_attractor = 0.0
        for i in range(self.dim):
            # Add periodic modulation with varying amplitudes
            periodic_attractor += (1.5 * np.sin(3 * x[i]) * np.cos(2 * x[i]) * 
                                 np.exp(-0.15 * np.abs(x[i])) + 
                                 0.8 * np.sin(5 * x[i]) * np.cos(4 * x[i]) * 
                                 np.exp(-0.1 * x[i]**2))
        
        # Gradient discontinuity field with piecewise linear behavior
        discontinuous = 0.0
        for i in range(self.dim):
            if x[i] < -2:
                discontinuous += 2.0 * np.sin(4 * x[i]) * np.exp(-0.3 * x[i]**2)
            elif x[i] > 2:
                discontinuous += 1.5 * np.cos(6 * x[i]) * np.exp(-0.4 * x[i]**2)
            else:
                discontinuous += 0.7 * np.sin(8 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        
        # Multi-scale fractal-like coupling with asymmetric interactions
        fractal_coupling = 0.0
        for i in range(self.dim - 1):
            # Asymmetric interaction with varying coupling strength
            if i % 2 == 0:
                fractal_coupling += 0.6 * np.sin(2.5 * x[i]) * np.cos(3.0 * x[i+1]) * \
                                  np.exp(-0.1 * (x[i] - x[i+1])**2)
            else:
                fractal_coupling += 0.4 * np.cos(3.5 * x[i]) * np.sin(2.0 * x[i+1]) * \
                                  np.exp(-0.15 * (x[i] + x[i+1])**2)
        
        # High-order polynomial with chaotic perturbations
        high_order = 0.0
        for i in range(self.dim):
            # Add cubic and quintic terms with chaotic modulations
            high_order += (0.3 * x[i]**3 + 0.2 * x[i]**5) * \
                         np.sin(7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Global scaling with variable fractal dimensionality
        global_scaling = 0.0
        for i in range(self.dim):
            global_scaling += 0.8 * np.sin(4 * x[i]) * np.cos(3 * x[i]) * \
                            np.exp(-0.05 * x[i]**2) * (1 + 0.2 * np.sin(9 * x[i]))
        
        # Combine all components with appropriate weights
        return base + 1.8 * chaotic_saddle + 1.2 * periodic_attractor + 1.0 * discontinuous + \
               0.7 * fractal_coupling + 0.5 * high_order + 0.6 * global_scaling