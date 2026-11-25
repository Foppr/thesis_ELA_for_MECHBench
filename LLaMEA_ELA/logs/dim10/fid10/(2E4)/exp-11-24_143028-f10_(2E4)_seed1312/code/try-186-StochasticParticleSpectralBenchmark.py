import numpy as np

class StochasticParticleSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Particle system parameters
        self.particle_count = max(10, dim * 2)
        self.time_step = 0.01
        self.damping = 0.95
        
        # Spectral interference parameters
        self.spectral_freqs = np.random.uniform(0.5, 3.0, dim)
        self.spectral_amps = np.random.uniform(0.5, 2.0, dim)
        
        # Evolutionary fitness landscape parameters
        self.generation = 0
        self.mutation_rate = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Stochastic particle system component with enhanced dynamics
        particle_sum = 0.0
        for i in range(min(5, self.dim)):  # Limit to first 5 dimensions for particle system
            # Simulate coupled harmonic oscillators with stochastic perturbations
            pos = x[i]
            velocity = np.sin(self.generation * 0.1 + pos) * 0.5
            acceleration = -pos * 0.8 + np.random.normal(0, 0.1)
            
            # Enhanced particle energy contribution with non-linear damping
            particle_sum += 0.5 * (velocity**2 + pos**2) + 0.3 * np.abs(acceleration) + 0.1 * np.sin(pos * 3)
        
        # Spectral wave interference component with enhanced complexity
        spectral_sum = 0.0
        for i in range(self.dim):
            # Create complex interference patterns using multiple frequencies and phases
            wave1 = self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i] + self.generation * 0.05)
            wave2 = self.spectral_amps[i] * np.cos(self.spectral_freqs[i] * x[i] * 1.5 + self.generation * 0.03)
            wave3 = 0.5 * self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i] * 2.0 + self.generation * 0.07)
            
            # Enhanced interference pattern with phase coupling
            spectral_sum += (wave1 * wave2 * wave3 + 
                           0.5 * np.sin(wave1 + wave2) + 
                           0.3 * np.cos(wave2 + wave3))
        
        # Evolutionary fitness landscape component with enhanced complexity
        fitness_sum = 0.0
        for i in range(self.dim):
            # Dynamic fitness landscape with moving optima and adaptive difficulty
            optimum_shift = np.sin(self.generation * 0.05 + i) * 2.0 + 0.5 * np.cos(self.generation * 0.03)
            distance_to_optimum = x[i] - (optimum_shift + np.sin(i) * 1.5)
            
            # Enhanced fitness function with multiple peaks, valleys and non-smooth regions
            fitness_sum += (distance_to_optimum**4 + 
                          0.5 * np.sin(3 * distance_to_optimum) * 
                          np.exp(-0.1 * distance_to_optimum**2) +
                          0.2 * np.sin(distance_to_optimum * 7) *
                          np.cos(distance_to_optimum * 5))
        
        # Cross-dimensional interaction terms with enhanced coupling
        interaction_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                # Enhanced coupled oscillatory behavior with adaptive coupling strength
                coupling_strength = 0.3 * (1 + np.cos(x[i] - x[j])) * (1 + 0.5 * np.sin(self.generation * 0.02))
                interaction_sum += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                                 np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Time-varying chaotic modulation with enhanced complexity
        chaotic_modulation = 0.0
        for i in range(self.dim):
            # Enhanced logistic map based on position and generation
            logistic_input = 3.9 * (x[i] / 5.0) * (1 - x[i] / 5.0)
            chaotic_modulation += np.sin(self.generation * 0.2 + logistic_input + 
                                       0.3 * np.sin(self.generation * 0.05)) * 0.5
        
        # Multi-scale Gaussian components with dynamic centers and adaptive widths
        gaussian_sum = 0.0
        for i in range(self.dim):
            # Multiple Gaussian peaks with time-varying positions, widths and heights
            center = 3.0 * np.sin(self.generation * 0.1 + x[i] * 0.5) + 0.8 * np.cos(self.generation * 0.03)
            width = 0.8 + 0.4 * np.cos(x[i]) + 0.2 * np.sin(self.generation * 0.04)
            height = 2.0 + 0.5 * np.sin(self.generation * 0.06)
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Final combined function with enhanced scaling and complexity
        result = particle_sum + spectral_sum + fitness_sum + interaction_sum + chaotic_modulation + gaussian_sum
        
        # Enhanced dynamic scaling based on generation with non-linear modulation
        dynamic_scaling = 1.0 + 0.1 * np.sin(self.generation * 0.02) + 0.05 * np.cos(self.generation * 0.04)
        result *= dynamic_scaling
        
        return result