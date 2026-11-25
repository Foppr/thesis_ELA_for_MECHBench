import numpy as np

class QuantumGeneticDeceptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum superposition parameters
        self.quantum_amplitudes = np.random.uniform(0.5, 2.0, size=dim)
        self.quantum_phases = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_angles = np.random.uniform(0, np.pi/2, size=dim)
        
        # Genetic algorithm parameters
        self.gene_length = np.random.randint(8, 16, size=dim)
        self.mutation_rate = np.random.uniform(0.01, 0.1, size=dim)
        self.crossover_rate = np.random.uniform(0.6, 0.9, size=dim)
        self.gene_weights = np.random.uniform(-1.0, 1.0, size=(dim, 10))
        
        # Dynamic fitness scaling
        self.scaling_factors = np.random.uniform(0.5, 3.0, size=dim)
        self.time_decay = np.random.uniform(0.01, 0.1, size=dim)
        self.fitness_shift = np.random.uniform(-2.0, 2.0, size=dim)
        
        # Deceptive trap components
        self.trap_centers = np.random.uniform(-4.5, 4.5, size=(5, dim))
        self.trap_radii = np.random.uniform(0.5, 3.0, size=5)
        self.trap_heights = np.random.uniform(1.0, 5.0, size=5)
        
        # Multi-objective fitness landscape
        self.objective_weights = np.random.uniform(0.1, 1.0, size=3)
        self.objective_shifts = np.random.uniform(-1.0, 1.0, size=3)
        
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 0.5, size=dim)
        self.noise_frequency = np.random.uniform(1.0, 5.0, size=dim)
        
        # Spatial correlation effects
        self.correlation_strength = np.random.uniform(0.2, 0.8, size=dim)
        self.correlation_distance = np.random.uniform(1.0, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum superposition component
        quantum_component = 0.0
        for i in range(self.dim):
            amp = self.quantum_amplitudes[i]
            phase = self.quantum_phases[i]
            angle = self.quantum_angles[i]
            quantum_val = amp * np.sin(angle * x[i] + phase)
            quantum_component += quantum_val
            
        # Genetic algorithm based fitness
        genetic_component = 0.0
        for i in range(self.dim):
            gene_sum = 0.0
            for j in range(10):
                gene_sum += self.gene_weights[i, j] * np.sin(x[i] * (j + 1))
            genetic_component += gene_sum
            
        # Dynamic fitness scaling with time decay
        scaling_component = 0.0
        for i in range(self.dim):
            scale_val = self.scaling_factors[i] * np.exp(-self.time_decay[i] * np.abs(x[i]))
            scaling_component += scale_val
            
        # Deceptive trap landscape
        trap_component = 0.0
        for i in range(5):
            dist = np.sqrt(np.sum((x - self.trap_centers[i]) ** 2))
            if dist <= self.trap_radii[i]:
                trap_val = self.trap_heights[i] * (1 - dist / self.trap_radii[i])
                trap_component += trap_val
                
        # Multi-objective fitness
        obj1 = np.sum(np.sin(x) ** 2)
        obj2 = np.sum(np.cos(x) ** 2)
        obj3 = np.sum(x ** 4)
        multi_obj_component = (self.objective_weights[0] * obj1 + 
                              self.objective_weights[1] * obj2 + 
                              self.objective_weights[2] * obj3)
        
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Spatial correlation effects
        correlation_component = 0.0
        for i in range(self.dim):
            corr_val = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    corr_val += self.correlation_strength[i] * np.exp(-dist / self.correlation_distance[i])
            correlation_component += corr_val
            
        # Combine all components with appropriate weights
        return (1.5 * quantum_component + 
                1.2 * genetic_component + 
                1.0 * scaling_component + 
                0.8 * trap_component + 
                0.6 * multi_obj_component + 
                0.4 * noise_component + 
                0.3 * correlation_component)