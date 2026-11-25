import numpy as np

class ChaoticHyperElasticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Hyper-elastic base potential with exponential stiffness modulation
        elastic_energy = 0.0
        for i in range(self.dim):
            # Exponential stiffness that varies with position and dimension
            stiffness = np.exp(2.0 * np.abs(x_scaled[i]))
            elastic_energy += 0.5 * stiffness * x_scaled[i]**2
        
        # Chaotic harmonic interactions with time-delayed coupling
        chaotic_interaction = 0.0
        for i in range(self.dim):
            # Add chaotic coupling with delayed influence from previous dimensions
            delayed_term = 0.0
            if i > 0:
                delayed_term = 0.3 * np.sin(x_scaled[i-1] * 2.0) * np.cos(x_scaled[i-1] * 1.5)
            
            # Main harmonic term with frequency modulation
            freq_mod = 1.0 + 0.5 * np.sin(x_scaled[i] * 3.0)
            chaotic_interaction += np.sin(freq_mod * x_scaled[i]) * \
                                 np.cos(freq_mod * x_scaled[i] * 0.7) * \
                                 np.exp(-0.5 * x_scaled[i]**2) + delayed_term
        
        # Multi-scale periodic potential with varying amplitude and frequency
        multiscale_potential = 0.0
        for scale in [1, 2, 3, 4, 6]:
            for i in range(self.dim):
                # Scale-dependent harmonic terms with phase shifts
                phase_shift = np.pi * scale / (self.dim + 1)
                multiscale_potential += (0.8 + 0.2 * np.sin(scale * x_scaled[i])) * \
                                       np.cos(scale * x_scaled[i] + phase_shift) * \
                                       np.exp(-0.1 * scale * np.abs(x_scaled[i]))
        
        # Coupling strength modulation with dimension-dependent weights
        coupling_strength = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Dimensionally weighted coupling with nonlinear interaction
                weight = (1.0 + 0.3 * np.sin(i * 0.5)) * (1.0 + 0.2 * np.cos(j * 0.7))
                coupling_strength += weight * (x_scaled[i] - x_scaled[j])**2 * \
                                   np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Boundary repulsion with tunable strength
        boundary_repulsion = 0.0
        for i in range(self.dim):
            # Quadratic repulsion from boundaries with dimension-specific strength
            strength = 1.5 + 0.5 * np.sin(i * 0.3)
            boundary_repulsion += strength * (np.abs(x_scaled[i]) - 1.0)**2 * \
                                np.exp(-0.5 * (np.abs(x_scaled[i]) - 1.0)**2)
        
        # Combine all components with modified weights for algorithm discrimination
        return 1.2 * elastic_energy + 0.8 * chaotic_interaction + 0.6 * multiscale_potential + \
               0.7 * coupling_strength + 0.5 * boundary_repulsion